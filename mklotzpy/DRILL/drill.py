import math

# Constants
PI = math.pi

# Function to calculate tap drill
def tap_drill(imperial=True):
    if imperial:
        tap_data = {
            "#0000": 0.021, "#000": 0.034, "#00": 0.047,
            "#0": 0.060, "#1": 0.073, "#2": 0.085,
            "#3": 0.099, "#4": 0.112, "#5": 0.125,
            "#6": 0.138, "#8": 0.164, "#10": 0.190,
            "#12": 0.216
        }

        print("Diameters of numbered taps:")
        for size, diameter in tap_data.items():
            print(f"{size} ({diameter*25.4:.3f} mm) = {diameter:.3f} in")

        tap_diameter = input("Tap Diameter (in): ")
        pitch = input("Pitch of Tap (threads/in): ")
    else:
        tap_diameter = input("Tap Diameter (mm): ")
        pitch = input("Pitch of Tap (mm/thread): ")

    dot = float(input("Percentage of material to remove with each step (%): "))
    af = float(input("Final Hole Size (in/mm): "))
    dp = float(input("Pilot Hole Size (in/mm): "))

    if imperial:
        td = float(tap_diameter)
        p = 1 / float(pitch)
    else:
        td = float(tap_diameter) / 25.4
        p = 1 / (float(pitch) / 25.4)

    aa = (5.0 / 8.0) * math.tan(math.radians(60.0))

    dtd = td - 0.01 * dot * aa / p

    print("\nTap Diameter =", td, "in =", td * 25.4, "mm")
    print("Tap Pitch =", p, "threads/in =", 1 / p, "in/thread")
    print("           =", p * 25.4, "threads/mm =", 25.4 / p, "mm/thread")
    print("Thread form constant used =", aa)

    print("\nTAP DRILL DIAMETER FOR", dot, "% DOT =", dtd, "in =", dtd * 25.4, "mm")

    return dtd

# Main function
if __name__ == "__main__":
    print("DRILL SIZES\n")
    
    while True:
        imperial = input("Choose unit system ([I]mperial or [M]etric, [Q] to Quit): ").lower()
        if imperial == 'i':
            imperial = True
            break
        elif imperial == 'm':
            imperial = False
            break
        elif imperial == 'q':
            exit()

    tap_drill(imperial)
