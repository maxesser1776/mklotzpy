import math

def main():
    print("TUBE SIZE FOR TURNING ECCENTRICS\n")

    # Input parameters
    D = float(input("Diameter of parent stock (in): "))
    e = float(input("Required eccentric offset (in): "))
    R = 0.5 * D
    r = R - e

    dtube = 2.0 * math.sqrt(7.0 * R * R - 9.0 * R * r + 3.0 * r * r)

    # Output the required tube diameter
    print(f"\nDiameter of required tube = {dtube:.4f} in")

if __name__ == "__main__":
    main()
