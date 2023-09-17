import math

# Utility functions
def vin(prompt, default, fmt, udef):
    while True:
        try: 
            value = float(input(f"{prompt}, [{default}]:") or default)
            return value
        except ValueError:
            print(f"Invalid input, Please enter a valid {fmt} value.")

# Main Function
def main():
    print("CUSP HEIGHT CALCULATIONS\n")

    # Initialize variables
    b = vin("Ball mill diameter (in)", 0.25, "1f", 0.25)
    c = vin("Desired cusp height (in)", 0.001, "1f", 0.001)
    r = 0.5 * b
    d = 2.0 * math.sqrt(2.0 * r * c - c * c) 

    # Print the spacing between successive cuts
    print(f"Spacing between successive cuts = {d:.4f} in")

if __name__ == "__main__":
    main()