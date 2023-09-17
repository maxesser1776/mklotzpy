import math

# Constants
NT = 500

# Global variables
nt = 0
th = [{'name': '', 'diam': 0.0, 'diamm': 0.0, 'pitch': 0.0, 'pitchm': 0.0} for _ in range(NT)]

# Function to read the data file
def read_data():
    global nt
    try:
        with open("FINDTHRD.DAT", "rt") as fpi:
            f = False
            for line in fpi:
                line = line.strip()
                if "STARTOFDATA" in line:
                    f = True
                    continue
                if not f:
                    continue
                if "ENDOFDATA" in line:
                    break
                if line and line[0] != ';':
                    parts = line.split()
                    if len(parts) < 5:
                        print(f"Skipping invalid line: {line}")
                        continue

                    th[nt]['name'] = parts[0]
                    try:
                        th[nt]['diam'] = float(parts[1])
                        th[nt]['diamm'] = float(parts[2])
                        th[nt]['pitch'] = float(parts[3])
                        th[nt]['pitchm'] = float(parts[4])
                    except ValueError:
                        print(f"Skipping invalid line: {line}")
                        continue

                    nt += 1
    except FileNotFoundError:
        print(f"FAILED TO OPEN DATA FILE: FINDTHRD.DAT")
        print("\a")


# Function to compare floats within a tolerance
def float_equals(a, b, tol_percent):
    tol = abs(tol_percent) / 100.0
    lower_bound = min(a, b) * (1.0 - tol)
    upper_bound = max(a, b) * (1.0 + tol)
    return lower_bound <= b <= upper_bound

# Main function
def main():
    global nt, th

    print("Search Andy Pugh's compilation of thread data\n")

    read_data()

    menu = """
A - Find thread from diameter in inches
B - Find thread from diameter in millimeters
C - Find thread from pitch in tpi (threads per inch)
D - Find thread from pitch in millimeters
M - Display this menu
Q - Quit
"""

    while True:
        print(menu)
        op = input("(A,B,C,D,M,Q) ? ").strip().lower()

        if op == 'q' or op == '27':
            break
        elif op == 'm':
            continue

        if op not in ['a', 'b', 'c', 'd']:
            print("NOT A VALID OPTION")
            print("\a")
            continue

        d = 0.0
        p = 0.0
        tol_percent = 1.0  # Default allowable error in percent

        if op in ['a', 'b']:
            d = float(input("Thread diameter: "))
            tol_percent = float(input("Allowable diameter error (%): "))
        elif op in ['c', 'd']:
            p = float(input("Thread pitch: "))
            tol_percent = float(input("Allowable pitch error (%): "))

        tol_percent = abs(tol_percent)  # Ensure it's positive

        a = 1.0 - tol_percent / 100.0
        b = 1.0 + tol_percent / 100.0

        print("\nName, diam (in), pitch (tpi), diam (mm), pitch (mm)\n")

        for i in range(nt):
            if op == 'a' and float_equals(d, th[i]['diam'], tol_percent):
                print(f"{i}: {th[i]['name']}, {th[i]['diam']:.4f}, {th[i]['pitch']:.4f}, {th[i]['diamm']:.4f}, {th[i]['pitchm']:.4f}")
            elif op == 'b' and float_equals(d, th[i]['diamm'], tol_percent):
                print(f"{i}: {th[i]['name']}, {th[i]['diam']:.4f}, {th[i]['pitch']:.4f}, {th[i]['diamm']:.4f}, {th[i]['pitchm']:.4f}")
            elif op == 'c' and float_equals(p, th[i]['pitch'], tol_percent):
                print(f"{i}: {th[i]['name']}, {th[i]['diam']:.4f}, {th[i]['pitch']:.4f}, {th[i]['diamm']:.4f}, {th[i]['pitchm']:.4f}")
            elif op == 'd' and float_equals(p, th[i]['pitchm'], tol_percent):
                print(f"{i}: {th[i]['name']}, {th[i]['diam']:.4f}, {th[i]['pitch']:.4f}, {th[i]['diamm']:.4f}, {th[i]['pitchm']:.4f}")

if __name__ == "__main__":
    main()
