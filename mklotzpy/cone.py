import math

def main():
    print("FLAT PATTERNS FOR CONICAL POARTS\n")

    d1 = float(input("small diameter of cone: "))
    d2 = float(input("large diameter of cone: "))
    x1 = float(input("height of cone: "))
    olap = float(input("overlap allowance for joining"))

    a = 0.5 * (d2 - d1)
    r = a / x1
    t1 = math.degrees(math.atan(r))
    st1 = math.sin(math.radians(t1))
    r1 = 0.5 * d1 / st1
    r2 = 0.5 * d2 / st1
    edge = r2 - r1

    if r1:
        z1 = (math.pi * d1 + olap) / r1
        c1 = 2.0 * r1 * math.sin(0.5 * z1)
    else: 
        c1 = 0.0

    z2 = (math.pi * d2 + olap) / r2
    c2 = 2.0 * r2 * math.sin(0.5 * z2)
    ang = z2 * (180.0 / math.pi)

    print(f"\nsmall diameter = {d1:.4f}")
    print(f"small circumfernece = {math.pi * d1:.4f}")
    print(f"large circumference = {math.pi * d2:.4f}")
    print(f"cone height = {x1:.4f}")
    print(f"overlap allowance = {olap:.4f}")

    print(f"\nIncluded angle of pattern + {ang:.4f} deg")
    print(f"smaller radius of pattern = {r1:.4f}")
    print(f"  chord of smaller radius = {c1:.4f}")
    print(f"   arc length for smaller radius = {ang * math.pi * r1 / 180.0:.4f}")
    print(f"length of edge = {edge:.4f}")
    print(f"cone included angle = {t1:.4f} deg")

if __name__ == "__main__":
    main()