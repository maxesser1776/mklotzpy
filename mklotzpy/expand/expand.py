import math

# Constants
ND = 200
DPR = 180.0 / math.pi

# Global variables
nd = 0
name = [""] * ND
cte = [0.0] * ND
mid = 0
opt = ""
rho = 0.0
length = 0.0
dlength = 0.0
deltat = 0.0

# Function to read the data file
def read_data():
    global nd
    with open("EXPAND.DAT", "rt") as fp:
        f = False
        for line in fp:
            line = line.strip()
            if "STARTOFDATA" in line:
                f = True
                continue
            if not f:
                continue
            if "ENDOFDATA" in line:
                break
            if line and line[0] != ';':
                parts = line.split(",")
                name[nd] = parts[0].strip()
                cte[nd] = float(parts[1].strip())
                nd += 1

# Function to compare strings for sorting
def acomp(v1, v2):
    l1 = len(v1)
    l2 = len(v2)
    l = min(l1, l2)
    for i in range(l):
        k = ord(v1[i].lower()) - ord(v2[i].lower())
        if k != 0:
            return k
    return (l1 - l2)

# Function to select material
def mselect():
    global nd
    for i in range(nd):
        print(f"{name[i]}={i + 1}  ")
    print(f"User input={nd + 1}")

    i = int(input("\n\nMaterial number: ")) - 1
    if i > nd - 1 or i < 0:
        i = nd

    if i == nd:
        cte[nd] = float(input("Material coefficient of thermal expansion (ppm/degF): "))
        name[nd] = "??"

    return i

# Main function
def main():
    global nd, mid, opt, rho, length, dlength, deltat

    print("MATERIAL EXPANSION CALCULATIONS\n")

    read_data()
    print(f"Number of data items read = {nd}")

    mid = mselect()

    rho = cte[mid] * 1.0e-6

    length = float(input("\nNominal length of object (in): "))

    agin = True
    while agin:
        print("\n A. Find length change given temperature change")
        print(" B. Find temperature change given length change")

        opt = input("([A],B) ? ").lower()
        if opt != 'b':
            opt = 'a'

        if opt == 'a':
            deltat = float(input("Temperature change (degF): "))
            dlength = rho * length * deltat
        elif opt == 'b':
            dlength = float(input("Length change (in): "))
            deltat = dlength / (rho * length)
        else:
            print("NOT A VALID OPTION")
            continue

        print(f"\nCTE of {name[mid]} = {rho * 1.0e6} ppm/degF")
        print(f"Nominal length = {length} in")
        print(f"Length change = {dlength} in")
        print(f"Temperature change = {deltat} degF")

        # Post-run processing
        agin = False

if __name__ == "__main__":
    main()
