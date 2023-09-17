import math

def main():
    print("CHORD LENGTH CALCULATION\n")

    nd = float(input("Number of divisions: "))
    diam = float(input("Diameter of circle: "))

    angle = 360 / nd
    chord = diam * math.sin(math.radians(0.5 * angle))

    print(f"Chord Length = {chord:.4f}")

if __name__ == "__main__":
    main()