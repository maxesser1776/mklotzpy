import math

# Constants
PI = math.pi

# Global variables
np = 0  # actual number of data items
pitch = []  # available thread pitches (tpi)
pc, pf, pe, best, tnc, tnf, dm = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

# Functions

def trim(s):
    return s.strip()

def rdata():
    global np, pitch

    dfile = "DIFFTHRD.DAT"
    f = False  # Flag to check if data entries are being read
    k = 0

    try:
        with open(dfile, "r") as fp:
            for line in fp:
                line = trim(line)
                if "STARTOFDATA" in line:
                    f = True
                    continue
                if not f:
                    continue
                if "ENDOFDATA" in line:
                    break
                if line.startswith("tp"):
                    k = 0
                    continue
                if line.startswith("mm"):
                    k = 1
                    continue
                if line and line[0] != ';':
                    # Decode and store data here
                    if k == 0:
                        pitch.append(float(line.split('\t')[0]))
                    else:
                        pitch.append(25.4 / float(line.split('\t')[0]))
                    np += 1

    except FileNotFoundError:
        print(f"FAILED TO OPEN DATA FILE: {dfile}")

    pitch.sort()  # Sort the pitch values in ascending order

def main():
    global np, pc, pf, pe, best, tnc, tnf, dm

    print("DIFFERENTIAL THREAD CALCULATIONS\n")
    print(f"Number of data items read = {np}\n")

    pe = float(input("Desired effective pitch of differential thread (tpi): "))

    if np == 0:
        print("No data items available.")
        return

    for p in pitch:
        if math.isclose(pe, p, rel_tol=1e-9):
            print("You can cut this thread directly with available screwcutting gear.")
            return

    best = float("inf")
    ib, jb = -1, -1

    for i in range(np):
        for j in range(np):
            if i == j:
                continue
            pc, pf = pitch[i], pitch[j]
            if pc > pf:
                pc, pf = pf, pc
            d = (1 / pc) - (1 / pf)
            e = abs(1 / d - pe)
            if e < best:
                best = e
                ib, jb = i, j

    print(f"\nOf available threads, best match to {pe:.3f} tpi is:")
    if ib != -1 and jb != -1:
        pc, pf = pitch[ib], pitch[jb]
        print(f"Coarse thread = {pc:.3f} tpi = {25.4 / pc:.3f} mm/thrd")
        print(f"Fine thread = {pf:.3f} tpi = {25.4 / pf:.3f} mm/thrd")
        print(f"with an effective pitch of {1 / (1 / pc - 1 / pf):.3f} tpi")

    pc = float(input("Pitch of coarse thread (tpi): "))
    pf = float(input("Pitch of fine thread (tpi): "))
    tnc = float(input("Thickness of coarse (fixed) nut (in): "))
    tnf = float(input("Thickness of fine (movable) nut (in): "))
    dm = float(input("Desired motion of movable nut (in): "))

if pc > 0 and pf > 0:
    pe = 1 / (1 / pc - 1 / pf)
    print(f"\nEffective pitch = {pe:.3f} tpi")
    print(f"Motion for one revolution = {1 / pe:.5f} in")
    print(f"Total turns to obtain desired motion = {dm * pe:.3f}")
    print(f"Minimum length of coarse thread needed = {tnc + dm * pe / pc:.3f} in")
    print(f"Minimum length of fine thread needed = {tnf + dm * pe / pf:.3f} in")
    print(f"Maximum distance between nuts = {dm * pe / pc:.3f} in")
    print(f"Minimum distance between nuts = {dm * pe / pf:.3f} in")
else:
    print("Error: Both pitch values (pc and pf) must be greater than zero.")


if __name__ == "__main__":
    rdata()
    main()
