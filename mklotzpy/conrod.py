import math 

def main():
    print("CONNECTING ROD CLEARNACE\n")

    print("Units of measurement don't matter but must be consistent")
    con1 = float(input("Connecting rod length (center-to-center): "))
    print("Radius measured from crank center to connecting rod driver center")
    radius = float(input("Crank radius: "))
    w = float(input("Height of cylinder bottom above crank center: "))
    d = float(input("Cylinder diameter: "))

    xa = math.sqrt(radius * radius + con1 * con1)
    cp = con1 / xa
    sp = radius / xa
    tp = sp / cp
    phi = math.degrees(math.acos(cp))
    d34 = 0.5 * d
    d45 = (xa - w) * tp
    d35 = d34 - d45
    d23 = d35 / cp
    d13 = d34 / cp
    d12 = d13 - d23
    d14 = d34 * tp
    d25 = d35 * sp

    print("\nAt worst case, maximum con rod lateral offset: ")
    print(f"Phi = {phi:.4f} deg")
    print(f"Distance, gudgeon pin to crank center = {xa:.4f}")
    print(f"d34 = {d34:.4f}")
    print(f"d45 = {d45:.4f}")
    print(f"d35 = {d35:.4f}")
    print(f"d23 = {d23:.4f}")
    print(f"d13 = {d13:.4f}")
    print(f"d12 = {d12:.4f}")
    print(f"d14 = {d14:.4f}")
    print(f"d25 = {d25:.4f}")

if __name__ == "__main__":
    main()
