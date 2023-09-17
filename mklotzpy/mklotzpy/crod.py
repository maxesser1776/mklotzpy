import math

# Function to calculate gudgeon pin position
def calculate_gudgeon_pin_position(crank_angle, throw, connecting_rod_length):
    crank_angle_rad = math.radians(crank_angle)
    gudgeon_pin_position = throw * math.cos(crank_angle_rad) + \
                           math.sqrt(connecting_rod_length**2 - throw**2 * math.sin(crank_angle_rad)**2)
    return gudgeon_pin_position

def main():
    print("Gudgeon Pin Position Calculator")

    # Input parameters
    connecting_rod_length = float(input("Enter connecting rod length: "))
    throw = float(input("Enter crank throw: "))
    crank_angle_increment = float(input("Enter angular increment (in degrees): "))

    print("\n{:>6} {:>10} {:>10}".format("Angle", "Gudgeon X", "Gudgeon Z"))
    
    for crank_angle in range(0, 181, int(crank_angle_increment)):
        gudgeon_x = calculate_gudgeon_pin_position(crank_angle, throw, connecting_rod_length)
        gudgeon_z = connecting_rod_length + throw - gudgeon_x
        print("{:>6} {:>10.3f} {:>10.3f}".format(crank_angle, gudgeon_x, gudgeon_z))

if __name__ == "__main__":
    main()
