import math

# Utility Functions
def vin(prompt, default, fmt, udef):
    while True:
        try:
            value = float(input(f"{prompt} [{default}]: ") or default)
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {fmt} value.")

# Main Function
def main(): 
    print("CYLINDRICAL COLLETS FOR POLYGONAL STOCK\n")

    # Initialize variables 
    n = int(vin("Number of stock polygon sides (n)", 6, "d", 6))
    af = vin("Stock across flats dimension (af)", 3/16, "1f", 3/16)
    sw = vin("Collet slot width (sw)", 0.045, "1f", 0.045)

    theta = 180.0 / n
    ct = math.cos(math.radians(theta))
    st = math.sin(math.radians(theta))

    d = 2.0 * math.sqrt(0.25 * sw * sw + (0.5 * af / ct - 0.5 * sw * st / ct) ** 2)

    # Print the required collet bore diameter
    print(f"\nRequired collet bore diameter = {d:4f} in")

if __name__ == "__main__":
    main()