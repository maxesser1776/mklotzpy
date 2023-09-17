import math

# Define constants
ND = 100

# Initialize global variables
name = ["" for _ in range(ND)]
fa = [0.0] * ND
fc = [0.0] * ND
nd = 0

# Function to read data from the file
def rdata():
    global nd
    with open("FITS.DAT", "rt") as fp:
        f = 0
        for line in fp:
            line = line.strip()
            if line == "STARTOFDATA":
                f = 1
                continue
            if not f:
                continue
            if line == "ENDOFDATA":
                break
            if line and not line.startswith(";"):
                parts = line.split(",")
                name[nd] = parts[0].strip()
                fc[nd] = float(parts[1].strip())
                fa[nd] = float(parts[2].strip())
                nd += 1
                if nd == ND:
                    print(f"More than maximum ({ND}) data items in data file")
                    exit(1)

# Function to calculate the diameter of the shaft for a selected fit
def calculate_shaft_diameter(selected_fit, nominal_diameter):
    nf = selected_fit - 1
    diam = nominal_diameter
    dc = diam + 0.001 * (fa[nf] * diam + fc[nf])
    return dc

# Main program
if __name__ == "__main__":
    print("SHAFT/HOLE FIT COMPUTATIONS\n")
    rdata()
    print(f"Number of data items read = {nd}\n")

    for i in range(nd):
        print(f"{i + 1}  {name[i]}")
    print()

    while True:
        try:
            selected_fit = int(input("Fit desired: "))
            if selected_fit < 1 or selected_fit > nd:
                print("OPTION SELECTION ERROR")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    nominal_diameter = float(input("Nominal diameter of shaft (in): "))
    dc = calculate_shaft_diameter(selected_fit, nominal_diameter)
    print(f"\nDiameter of shaft for {name[selected_fit - 1]} Fit = {dc:.5f} in")
