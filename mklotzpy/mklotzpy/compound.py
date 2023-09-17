import math

def dms(a):
    d = int(abs(a))
    sgn = ' ' if a >= 0 else '-'
    f = abs(a) % 1 * 3600
    m, f = divmod(f, 60)
    s, f = divmod(f, 1)
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        d += 1
    return f"{sgn}{d} deg, {int(m)} min, {int(s)} sec"

def main():
    print("SETTING COMPOUND REST ANGLE\n")

    while True:
        try:
            ratio = float(input("Required movement ratio: "))
            if ratio <= 1.0:
                break
            else:
                print("Ratio must be <= 1")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    angle = math.degrees(math.asin(ratio))
    complement_angle = 90 - angle

    print(f"Set compound angle to {angle:.4f} deg = {dms(angle)}")
    print(f"Complement of this angle = {complement_angle:.4f} deg = {dms(complement_angle)}")

if __name__ == "__main__":
    main()
