import math

def calculate_cone_depth(sphere_radius, cone_base_radius, cone_apex_angle_degrees):
    # Convert the cone apex angle from degrees to radians 
    cone_apex_angle_radians = math.radians(cone_apex_angle_degrees)

    # Calculate the cone depth using the formula
    cone_depth = (sphere_radius - cone_base_radius) * (1 - math.cos(cone_apex_angle_radians))

    return cone_depth

# Input values
sphere_radius = float(input("Enter the radius of the sphere: "))
cone_base_radius = float(input("Enter the radius of the cone's base: ")) 
cone_apex_angle_degrees = float(input("Enter the cone apex in degrees: "))

# Calculate the cone depth
result = calculate_cone_depth(sphere_radius, cone_base_radius, cone_apex_angle_degrees)

# Display the result
print(f"The cone depth is: {result}")