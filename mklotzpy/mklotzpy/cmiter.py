import math

def main():
    print("TABLE SAW ANGLES FOR POLYGON FORMS\n")

    n = int(input("Numbers of sides: "))
    s = float(input("Slop (in degrees): "))
    print()

    print(f"Number of sides = {n}")
    print(f"Slope = {s:.4f} deg")

    if s == 90.0:
        mg = 90.0
        btm = 180.0 / n
        btb = 0 
    elif s == 0.0:
        mg = math.degrees(math.atan(1.0 / (math.cos(math.radians(s)) * math.tan(math.radians(180.0 / n)))))
        btm = 0
        btb = 90

    else:
        mg = math.degrees(math.atan(1.0 / (math.cos(math.radians(s) * math.tan(math.radians(180.0 / n))))))
        cmg = math.cos(math.radians(mg))
        ts = math.tan(math.radians(s))
        btm = math.degrees(math.atan(cmg * ts))
        btb = math.degrees(math.atan(cmg / ts))

    print(f"Mister gauge angle = {mg:.4f} deg")
    print(f"Blade titlt (Mitered) = {btm:.4f} deg")
    print(f"Blade tilt (butted) = {btb:.4f} deg")

if __name__ == "__main__": 
    main()