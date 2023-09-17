
import math

def main():
    print("BEND ALLOWANCE COMPUTATION\n")
    t = float(input("Thickness of material (in): "))  # Input thickness
    r = float(input("Radius of bend (in): "))        # Input bend radius
    ang_deg = float(input("Angle of bend (deg): "))   # Input bend angle in degrees

    ang_rad = math.radians(ang_deg)  # Convert angle to radians
    x = 0.4 * t
    if r < 2.0 * t:
        x = 0.33333 * t
    if r > 4.0 * t:
        x = 0.5 * t

    ba = ang_rad * (r + x)

    print("\nLength of bend exterior = {:.4f} in".format(ang_rad * (r + t)))
    print("Length of bend interior = {:.4f} in".format(ang_rad * r))
    print("\nLength of material required to form bend = {:.4f} in".format(ba))

if __name__ == "__main__":
    main()
