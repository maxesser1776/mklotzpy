import math

# Constants
DPR = 180.0 / math.pi

# Function to calculate division plate
def division_plate():
    ndiv = int(input("Number of divisions: "))
    dc = float(input("Diameter of mounting circle: "))
    rc = dc / 2.0
    theta = 360.0 / ndiv
    s = math.sin(math.radians(theta / 2.0))
    rd = rc * s / (1.0 - s)
    print("\nDIVISION PLATE CALCULATION\n")
    print(f"Number of divisions = {ndiv}")
    print(f"Diameter of mounting circle = {dc}")
    print(f"Disk diameter = {2.0 * rd}")

if __name__ == "__main__":
    division_plate()
