import math

# Constants
MAXLENGTHS = 100  # Maximum number of lengths to be used
MAXPIECESPERLENGTH = 100  # Maximum number of pieces per length of stock
MAXPIECES = 1000  # Maximum number of pieces to be cut

# Global variables
np = 0  # actual number of object sizes
num = [0] * MAXPIECES  # number needed
npiece = 0  # number of pieces needed
size = [0.0] * MAXPIECES  # object sizes
precision = 1.0e-3  # used in comparing reals
bars = [0.0] * MAXLENGTHS  # storage for remnant sizes
nbars = 0  # actual number of remnants
maxbar = 0.0  # length of longest remnant
tbars = 0.0  # total length of remnants
reqd = 0.0  # total required pieces length
kreqd = 0.0  # total required length including kerf
waste = 0.0  # total waste
kerf = 0.0  # saw kerf width
kwaste = 0.0  # total kerf waste
dwaste = 0.0  # total drop waste
pieces = []  # sizes to cut

# Structure for stock lengths
class StockLength:
    def __init__(self):
        self.cuts = 0  # number of pieces cut from this length
        self.bar = 0.0  # original bar length
        self.drop = 0.0  # unallocated length
        self.size = []  # sizes of pieces

# List of StockLength objects
stock = [StockLength() for _ in range(MAXLENGTHS)]


def diff(a, b):
    t = a - b
    return 0 if abs(t) <= precision else 1 if t > 0 else -1


def rdata():
    global np, kerf, nbars, maxbar, tbars, reqd, kreqd, npiece

    dfile = "REMNANT.DAT"
    ff = True  # Flag to check if kerf is read
    f = True  # Flag to check if remnants are being read

    try:
        with open(dfile, "r") as fp:
            for line in fp:
                line = line.strip()
                if "ENDOFDATA" in line:
                    break
                if line and line[0] != ';':
                    parts = line.split(';')[0].split('\t')  # Remove comments and split by tabs
                    if ff:
                        kerf = float(parts[0])  # Read the first part as kerf
                        ff = False
                    else:
                        if f:
                            data_parts = parts[0].split(',')  # Split by comma to handle multiple remnants
                            for data_part in data_parts:
                                data_values = data_part.split()
                                if len(data_values) == 2:
                                    k, t = map(float, data_values)  # Split and convert to float
                                    if k == 0:
                                        f = False
                                        continue
                                    if t > maxbar:
                                        maxbar = t
                                    for _ in range(int(k)):
                                        bars[nbars] = t
                                        tbars += t
                                        nbars += 1
                        else:
                            data_values = parts[0].split()
                            if len(data_values) == 2:
                                num_part, size_part = map(float, data_values)  # Split and convert to float
                                num[np] = int(num_part)
                                size[np] = size_part
                                npiece += num[np]
                                reqd += num[np] * size[np]
                                kreqd += num[np] * (size[np] + kerf)
                                np += 1

    except FileNotFoundError:
        print(f"Failed to open data file: {dfile}")

    # Sort the data
    for i in range(np):
        for j in range(np - 1):
            if size[j] < size[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
                size[j], size[j + 1] = size[j + 1], size[j]

    for i in range(nbars):
        for j in range(nbars - 1):
            if bars[j] < bars[j + 1]:
                bars[j], bars[j + 1] = bars[j + 1], bars[j]




def cutlist():
    global nbars, npiece, tbars, kwaste, dwaste

    i = 0
    tcuts = 0  # Initialize tcuts here
    best = 0

    for i in range(numpieces):
        j = 0
        while stock[j].drop - pieces[i] < 0:
            j += 1
        best = j
        if best > MAXPIECESPERLENGTH:
            print(f"*** PIECE {pieces[i] - kerf} CAN'T BE ASSIGNED ***")
            continue

        while stock[j + 1].bar != 0:
            if stock[best].drop > stock[j + 1].drop and stock[j + 1].drop >= pieces[i]:
                best = j + 1
            j += 1

        stock[best].drop -= pieces[i]
        stock[best].size.append(pieces[i])
        stock[best].cuts += 1

    i = 0
    while stock[i].bar != 0:
        tcuts += stock[i].cuts  # Update tcuts here
        kw = tcuts * kerf
        kwaste += kw
        dwaste += stock[i].drop
        print(f"Length {stock[i].bar} - ", end="")
        for j in range(tcuts):
            print(f"{stock[i].size[j] - kerf}, ", end="")
        print(f"({kw} kerf + {stock[i].drop} drop = {stock[i].drop + kw} waste)")
        i += 1

    if tcuts < npiece:
        print(f"\n*** WARNING: {npiece - tcuts} PIECE(S) NOT ASSIGNED ***")

    print(f"\ntheoretical possible waste = {tbars} - {reqd} = {tbars - reqd}")
    print(f"kerf waste = {kwaste}")
    print(f"drop waste = {dwaste}")
    print(f"kerf + drop waste = {kwaste + dwaste}")



def main():
    global maxbar, kerf, np, bars, nbars, tbars, reqd, npiece, size, num, waste, pieces, numpieces

    print("REMNANT CUTTING LIST\n")
    rdata()
    print(f"saw kerf = {kerf}")
    print("remnants =", end=" ")
    for i in range(nbars):
        print(f"{bars[i]}, ", end="")
    print()
    print(f"total remnant pieces, length = {nbars}, {tbars}")
    print(f"total required pieces length = {reqd}\n")

    if size[np - 1] > maxbar:
        print(f"largest piece {size[np - 1]} larger than largest remnant {maxbar}")
        return

    if reqd > tbars:
        print(f"total piece length {reqd} greater than total remnant length {tbars}")
        return

    if kreqd > tbars:
        print(f"total piece length including kerf allowance {kreqd} greater than total remnant length {tbars}")
        return

    if size[0] > maxbar:
        print(f"smallest piece {size[np - 1]} longer than shortest remnant {maxbar}\n")

    print("\t", end="")
    for i in range(np):
        print(num[i], end="\t")
    print()

    print("\t", end="")
    for i in range(np):
        print(f"{size[i]:.2f}", end="\t")
    print()

    # Construct the pieces array
    for i in range(np):
        for j in range(num[i]):
            pieces.append(size[i] + kerf)
    numpieces = len(pieces)

    # Store the stock data
    for i in range(nbars):
        stock[i].bar = bars[i]
        stock[i].drop = bars[i]

    cutlist()


if __name__ == "__main__":
    main()
