import math
import re

# Constants
N = 100

# Global variables
np = 0
num = [0] * N
size = [0] * N
bar = 0.0
best = [0] * N
last = [0] * N
precision = 1.0e-3
debug = False

# Function to compare two real numbers with a given precision
def diff(a, b):
    t = a - b
    return 0 if abs(t) <= precision else 1 if t > 0 else -1

# Function to read the data file
def rdata():
    global np, bar

    try:
        with open("CUTS.DAT", "r") as fp:
            lines = fp.readlines()
            for line in lines:
                line = line.strip()
                if line == "ENDOFDATA":
                    break
                if line and line[0] != ';':
                    parts = re.split(r'[\t,]', line)  # Split using both tabs and commas
                    if not bar:
                        bar = float(parts[0])
                    else:
                        num[np] = int(parts[0])
                        size[np] = float(parts[1])
                        np += 1
    except FileNotFoundError:
        print("Failed to open data file: CUTS.DAT")


# Function to find the best greedy combination
def greedy(zeroflag):
    global best, np, bar, size, num

    max_pieces = [min(math.ceil(bar / s), n) if s != 0 else 0 for s, n in zip(size, num)]
    x = max_pieces.copy()
    waste = 1.0e9
    score = 0.0

    while True:
        len_comb = sum(x[i] * size[i] for i in range(np))
        if diff(len_comb, bar) > 0:
            break

        if all(x[i] <= num[i] for i in range(np)):
            s = sum(x[i] * (0.5 ** i) for i in range(np))
            w = bar - len_comb if diff(bar - len_comb, 0) != 0 else 0.0

            if zeroflag == 0 and w != 0.0:
                continue

            if bar != 0 and w < bar:
                score = s
                waste = w
                best = x.copy()

        k = 0
        while k < np and x[k] == 0:
            k += 1
        if k >= np:
            break

        x[k] -= 1
        for i in range(k):
            x[i] = max_pieces[i]

    return waste

# Main function
def main():
    global best, last, debug

    print("Optimize cutting pieces from bars of standard length.")
    print("Uses a modified greedy algorithm.\n")

    rdata()
    print(f"Number of data items read = {np}")
    reqd = sum(size[i] * num[i] for i in range(np))
    oreqd = math.ceil(reqd / bar) if bar != 0 else 0
    owaste = oreqd * bar - reqd
    print(f"Standard length = {bar}")
    if size[0] > bar:
        print(f"Largest piece {size[0]} larger than bar {bar}")
        return
    print(f"Theoretical minimum waste possible = {owaste}")
    print(f"Theoretical minimum standard lengths possible = {oreqd}\n")
    print("\t" + "\t".join(str(num[i]) for i in range(np)))
    print("\t" + "\t".join(f"{size[i]:.2f}" for i in range(np)))
    print()

    op = input("Search for zero waste solutions first (Y/[N]) ? ").lower()
    debug = True if op == 'y' else False
    dup = 1 
    if debug:
        op = 'y'
        waste = greedy(0)
        if waste > 1.0e8:
            waste = greedy(1)
        print(f"Best solution found = {best}, Waste = {waste}")
    else:
        op = 'n'
        waste = greedy(1)

    nbar = 1
    twaste = waste
    last = best.copy()

    while True:
        more = False
        for i in range(np):
            if num[i] - best[i] > 0:
                more = True
                break
        
        if waste == bar:
            more = False

        if nbar > 1:
            k = 0
            while k < np:
                if best[k] != last[k]:
                    break
                k += 1
            if k < np:
                k = 1
            else:
                k = 0

        else:
            k = 0
            dup = 2

        if not k:
            k += 1

        if not bar:
            print("Bar length is zero. Cannot proceed.")
            break

        if not more:
            k += 1

        if k:
            waste = greedy(0) if op == 'y' else greedy(1)
            nbar += 1
            twaste += waste

            for i in range(np):
                if num[i] - best[i] > 0:
                    more = True
                    break

            if waste == bar:
                more = False

            last = best.copy() # Move this line here
            lwaste = waste

            if k:
                print(f"{k} x {' x '.join(map(str, last))}  {dup * lwaste}")

            else:
                k += 1

        if not more:
            print(f"{k} x {' x '.join(map(str, last))}  {dup * lwaste}\n")
            print(f"Actual waste = {twaste}")
            print(f"Actual standard lengths = {nbar}")
            break

if __name__ == "__main__":
    main()
