import math

# Utility functions
def vin(prompt, default, fmt, udef):
    while True:
        try: 
            value = float(input(f"{prompt} [{default}]: ") or default)
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {fmt} value.")

# Main function
def main():
    print("DRILL TIP ALLOWANCE COMPUTATION\n")

    # Initialize variables
    theta = vin("Included angle of drill tip (thea)", 118.0, "1f", 118.0)
    tz = math.tan(math.radians(0.5 * theta))
    dh = vin("Drill diameter (dh)", 0.5, "1f", 0.5)

    a = 0.5 * dh / tz

    # Print the allowance for drill tip
    print(f"\nAllowance for drill tip = {a:.4f} in")

if __name__ == "__main__":
    main()