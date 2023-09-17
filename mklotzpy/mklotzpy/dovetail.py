import math

# Constants
RPD = math.pi / 180.0
DPR = 180.0 / math.pi

# Function to calculate dovetail measurements
def dovetail_measurements():
    mf = input("(M)ale or (F)emale dovetail ? ").lower()
    if mf != 'm' and mf != 'f':
        print("Error, please try again")
        return

    angle = float(input("Dovetail angle (degrees): "))
    pin = float(input("Pin diameter: "))

    if mf == 'm':
        h = float(input("Height of dovetail: "))
        x = float(input("Measurement across pins: "))
    else:
        h = float(input("Depth of dovetail: "))
        x = float(input("Measurement between pins: "))

    c = h / math.tan(math.radians(angle))
    ta = math.tan(math.radians(0.5 * angle))
    q = 1.0 + 1.0 / ta

    if mf == 'm':
        b = x - pin * q
        t = b + 2.0 * c
    else:
        b = x + pin * q
        t = b - 2.0 * c

    print("\nDOVETAIL MEASUREMENTS\n")
    print(f"Dovetail angle = {angle:.4f} degrees")
    print(f"Pin diameter = {pin:.4f}")
    print(f"Measurement across pins = {x:.4f}")
    print(f"Height of dovetail = {h:.4f}")
    print(f"Measurement across top of dovetail = {t:.4f}")
    print(f"Measurement across bottom of dovetail = {b:.4f}")

if __name__ == "__main__":
    dovetail_measurements()
