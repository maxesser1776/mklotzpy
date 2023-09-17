import math

# Utility functions
def vin(prompt, default, fmt, udef):
    while True:
        try:
            value = float(input(f"{prompt} [{default}]: ") or default)
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {fmt} value.")

def get_int_input(prompt, default):
    while True:
        user_input = input(f"{prompt} [{default}]: ").strip()
        if user_input == "":
            return default # Use the default value if input is empty 
        try:
            value = int(user_input)
            return value
        except ValueError:
            print("Invalid input. Please enter a valid intergear.") 

def get_float_input(prompt, default):
    while True: 
        user_input = input(f"{prompt} [{default}]: ").strip()
        if user_input == "":
            return default # Use the default value if input is empty
        try:
            value = float(user_input)
            return value
        except ValueError: 
            print("Invalid input. Please enter a valid float.")

# Main function
def main():
    print("(DIFFERENTIAL) DIVIDING HEAD CALCULATIONS\n")

    # Initialize variables
    ratio = get_float_input("DH Worm Gear Ratio", 40)
    divisions = get_int_input("Number of workpiece divisions", 67)
    rholes = -999
    holes = []
    nh = 0
    gear = []
    ng = 0
    pacc = 0.01

    nd = 0  # Number of data entries
    nl = 1  # Number of gear pair loops
    maxpair = 1  # Maximum gear pairs to examine
    printflag = 0  # Flag to indicate if a solution is printed

    print("Reading data from file...")

    with open("DDH.DAT", "r") as fpt:
        for line in fpt:
            line = line.strip()
            if line.startswith("STARTOFDATA"):
                continue
            elif line.startswith("ENDOFDATA"):
                break

            if line:
                data = line.split(",")
                if ratio < 0:
                    ratio = int(data[0])
                elif rholes == -999:
                    rholes = int(data[0])
                else:
                    j = int(data[0])
                    if j == -1:
                        break
                    else:
                        holes.append(j)
                        nh += 1

                nd += 1

    holes.sort()

    # Find gear solutions
    print("Finding gear solutions...")

    for ihole in range(nh):
        p = holes[ihole]
        x = ratio * p / divisions
        ininc = math.floor(x)

        for jj in range(ininc - 2, ininc + 3):
            approx = ratio * p / jj
            rnum = abs((approx - divisions) * ratio)
            rdenom = approx

            if rnum == 0:
                continue

            result = fgear(rnum / rdenom, p, jj)
            if result == -1:
                return

    if not printflag:
        print("\nNO SOLUTION USING DIFFERENTIAL INDEXING WAS FOUND")
        return

    print("\nYour data is on: DDH.OUT")

# fgear function
def fgear(ratio, p, jj):
    global nl, maxpair, printflag, pacc

    printflag = 0

    if maxpair > 1:
        print("\nPatience... Press any key to abort")

    ihole = 0
    flag = 0

    while ihole < nh:
        p = holes[ihole]
        x = ratio * p / divisions
        ininc = math.floor(x)

        for j in range(ininc - 2, ininc + 3):
            approx = ratio * p / j
            rnum = abs((approx - divisions) * ratio)
            rdenom = approx

            if rnum == 0:
                continue

            result = fgear_inner(rnum / rdenom, p, j)
            if result == -1:
                return

            if result > 0:
                flag += 1

        ihole += 1

    if not flag:
        print("\nNO SOLUTION USING DIFFERENTIAL INDEXING WAS FOUND")
    else:
        print("\nYour data is on: DDH.OUT")

def fgear_inner(ratio, p, jj):
    global nl, maxpair, printflag, pacc

    index = [0] * nl  # Initialize indices
    index_copy = [0] * nl

    c = '-'

    for l in range(nl):
        index[l] = llimit[l]  # Initialize indices

    while True:
        if kbhit():
            print("\nRUN ABORTED BY USER")
            return -1

        for i in range(nl):
            gear_ratio = gear[gj[i]] / gear[gk[i]]
            if gear_ratio == 1:
                continue

            if ratio > 1:
                ratio *= gear_ratio
            else:
                ratio /= gear_ratio
                gk[i] *= -1

        error = 100 * (ratio - divisions) / divisions

        if abs(error) > pacc:
            continue

        if not printflag:
            with open("DDH.OUT", "w") as fp:
                fp.write("------------\n\n")
                fp.write(f"Hole plate = {p}\n")
                fp.write(f"Indexing increment = {jj}\n")
                if approx > divisions:
                    fp.write("Hole plate and crank rotate in the same direction\n")
                if approx < divisions:
                    fp.write("Hole plate and crank rotate in opposite directions\n")
                fp.write(f"Gear ratio = {rnum} / {rdenom} = {rnum / rdenom}\n")
                fp.write("\nAcceptable gear trains include:\n\n")
                printflag = 1

        gear_pairs = [
            f"{c}{gear[gj[i]]}:{gear[gk[i]]}" if gk[i] > 0 else f"{c}{gear[gk[i]]}:{gear[gj[i]]}"
            for i, c in enumerate("-" * nl)
        ]

        with open("DDH.OUT", "a") as fp:
            fp.write("  ".join(gear_pairs))
            fp.write(f"  {ratio}  {error:.3E}%\n")

        return 1

if __name__ == "__main__":
    divisions = 67  # Define 'divisions' here
    main()
