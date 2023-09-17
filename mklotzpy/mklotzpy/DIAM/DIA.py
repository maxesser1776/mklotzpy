import math

# Constants
PI = math.pi

# Global variables
nd = 0  # actual number of data entries
name = []  # material names
lo = []  # low values of sfpm
hi = []  # high values of sfpm
nm = 0  # material number
d = 0.0  # diameter
low, high = 0.0, 0.0  # recommended rpm
ns = 0  # number of machine speeds
speed = []  # available machine speeds (rpm)
dlow, dhigh = 0.0, 0.0  # diameters corresponding to speeds and material
c = 12 / PI

# Functions

def trim(s):
    return s.strip()

def rdata():
    global nd, name, lo, hi, ns, speed
    
    dfile = "DIAM.DAT"
    f = False  # Flag to check if data entries are being read

    try:
        with open(dfile, "r") as fp:
            for line in fp:
                line = trim(line)
                if "ENDOFDATA" in line:
                    break
                if "SPEEDS" in line:
                    f = True
                    continue
                if line and line[0] != ';':
                    if f:
                        try:
                            speed.append(float(line.split('\t')[0]))
                            ns += 1
                        except ValueError:
                            continue
                    else:
                        parts = line.split('\t')
                        if len(parts) >= 3:
                            try:
                                name.append(parts[0])
                                lo.append(float(parts[1]))
                                hi.append(float(parts[2]))
                                nd += 1
                            except ValueError:
                                continue

    except FileNotFoundError:
        print(f"FAILED TO OPEN DATA FILE: {dfile}")

# Main function
def main():
    global ns, nm, nd, name, lo, hi, d, low, high, speed, dlow, dhigh, c

    print("MACHINING DIAMETER UTILITY\n")
    rdata()
    print(f"number of data entries read = {nd}\n")

    for i in range(nd):
        print(f"{i + 1:4d}  {name[i]}")
        if (i + 1) % 15 == 0:
            input("press a key\n")

    ofile = "DIAM.OUT"

    try:
        with open(ofile, "wt") as fp:
            while True:
                nm = int(input("Material Number: ")) - 1
                if nm < 0 or nm > nd - 1:
                    print("INVALID NUMBER")
                    continue
                break

            fp.write(f"Material = {name[nm]}\n\n")
            fp.write("SPEED    DMIN    DMAX\n")
            fp.write(" rpm      in      in\n\n")

            for i in range(ns):
                dlow = c * lo[nm] / speed[i]
                dhigh = c * hi[nm] / speed[i]
                fp.write(f"{speed[i]:6.0f}  {dlow:6.3f}  {dhigh:6.3f}\n")

        print(f"\nYour data is on: {ofile}")

    except IOError:
        print(f"FAILED TO OPEN OUTPUT FILE: {ofile}")

if __name__ == "__main__":
    main()
