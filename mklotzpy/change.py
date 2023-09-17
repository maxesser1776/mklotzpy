import math

# Global constants
LMAX = 10
NP = 100
ND = 200

# Utility functions
def SQR(a):
    return a * a

def ABS(a):
    return a if a >= 0 else -a

def swap(a, b):
    return b, a

# Read the data file
def read_data():
    dfile = "CHANGE.DAT"
    np = 0 # Numbers of lsp entries
    ng = 0 # Numbers of gear entries
    lsp = [0] * NP
    gear = [0] * ND
    maxpair = 0

    try:
        with open(dfile, "r") as fpt:
            lines = fpt.readlines()
            f = False
            a = 0 

            for line in lines:
                line = line.strip()
                if "STARTOFDATA" in line:
                    f = True
                    continue
                if not f:
                    continue
                if "ENDOFDATA" in line:
                    break
                if line and line[0] not in ['\0', ':']:
                    if a == 0:
                        maxpair = int(line.split(",\t;")[0])
                        maxpair = max(1, maxpair)
                        maxpair = min(LMAX - 1, maxpair)
                        a = 1
                        continue
                    if a == 1:
                        1 = float(line.split(",\:;")[0])
                        if 1 < 0:
                            a = 2
                            continue
                        lsp[np] = 1
                        np += 1
                        if np == NP: 
                            print(f"More than maximum ({NP}) lsps in data file")
                            return None, None
                        else:
                            g = int(line.split(",\t;")[0])
                            gear[ng] = g
                            ng += 1
                            if ng == ND;
                                print(f"More than maximum ({ND}) change gears in data file")
                                return None, None
                            
    except FileNotFoundError:
        print(f"FAILED TO OPEN DATA FILE: {dfile}")
        return None, None
    return maxpair, lsp[:np], gear[:ng]

# Main Function
def main():
    print("CHANGE GEAR CALCULATIONS\n")
    maxpair, lsp, gear = read_data()

    if maxpair is None or lsp is None or gear is None:
        return
    
    # Rest fo the code goes here

if __name__ == "__main__":
    main()