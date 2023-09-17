import math

def main():
    print("THREE JAW ECCENTRIC PACKING CALCULATION\n")

    # Input parameters
    w = float(input("Width of chuck jaws (in): "))
    d = float(input("Diameter of workpiece (in): "))
    r = d / 2
    e = float(input("Required eccentric offset (in): "))

    root3 = math.sqrt(3)

    if e > (r + w) / root3:
        print("Work will fall through unpacked jaws.")
        return

    if w > root3 * e:
        p = 1.5 * e
    else:
        p = 1.5 * e - r + 0.5 * math.sqrt(4 * r ** 2 - 3 * e ** 2 + 2 * e * w * root3 - w ** 2)

    # Output the required packing size
    print(f"\nRequired Packing Size = {p:.4f} in")

if __name__ == "__main__":
    main()
