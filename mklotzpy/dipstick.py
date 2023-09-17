import math

# Constants
PI = math.pi

# Function to calculate the wetted fraction for a horizontal cylindrical tank
def fcyl(h, r):
    z = r - h
    angle = 2.0 * math.acos(z / r)
    chord = 2.0 * r * math.sin(0.5 * angle)
    area = 0.5 * (r * r * angle - z * chord)
    return area

# Function to calculate the wetted fraction for a spherical tank
def fspher(h, r):
    return h * h * (3 * r - h) / (4 * r * r * r)

# Function to calculate the wetted fraction for an elliptical tank
def fellip(h, a, b):
    area = (a / b) * ((h - b) * math.sqrt(h * (2 * b - h)) + b * b * (math.asin((h - b) / b) + 0.5 * PI))
    return area

# Function to calculate the wetted fraction for a vertical cartouche
def fvcart(h, a, b, r, l):
    if h <= r:
        z = r - h
        angle = 2.0 * math.acos(z / r)
        chord = 2.0 * r * math.sin(0.5 * angle)
        area = 0.5 * (r * r * angle - z * chord)
    elif r < h <= (r + l):
        area = 0.5 * PI * r * r + a * (h - r)
    else:
        z = r - (h - l)
        angle = 2.0 * math.acos(z / r)
        chord = 2.0 * r * math.sin(0.5 * angle)
        area = 0.5 * (r * r * angle - z * chord) + l * a
    return area

# Function to calculate the wetted fraction for a horizontal cartouche
def fhcart(h, a, b, r, l):
    z = r - h
    angle = 2.0 * math.acos(z / r)
    chord = 2.0 * r * math.sin(0.5 * angle)
    area = 0.5 * (r * r * angle - z * chord) + h * l
    return area

# Function to calculate the wetted fraction for a bucket
def fbuck(h, hb, rb, rs):
    r = rs + (rb - rs) * h / hb
    z = rs * rs + rs * r + r * r
    vol = PI * h * z / 3.0
    return vol

# Function to calculate the wetted fraction for a barrel
def fbarrel(h, hb, rb, rs):
    vol = PI * (rb * rb * h + (rs * rs - rb * rb) * (hb * hb * h - 2.0 * hb * h * h + 4.0 * h * h * h / 3.0) / (hb * hb))
    return vol

# Function to calculate the wetted fraction for a horizontal cylindrical tank with hemispherical ends
def fhcyl(h, r, a, d):
    z = r - h
    angle = 2.0 * math.acos(z / r)
    chord = 2.0 * r * math.sin(0.5 * angle)
    area = 0.5 * (r * r * angle - z * chord)
    vc = area * (a - d)
    vh = PI * h * h * (r - h / 3.0)
    return (vc + vh)

# Function to calculate the wetted fraction for a horizontal cylindrical tank with dished ends
def fdcyl(h, r, l1, l2):
    z = r - h
    angle = 2.0 * math.acos(z / r)
    chord = 2.0 * r * math.sin(0.5 * angle)
    area = 0.5 * (r * r * angle - z * chord)
    vc = area * l2
    hdish = 0.5 * (l1 - l2)
    vd = PI * hdish * (3.0 * r * r + hdish * hdish) / 6.0
    return (vc + 2.0 * vd)

# Function to perform binary search for wetted dipstick length
def binsearch(l, r, val, tol, func, *args):
    i = 0
    while True:
        x = l + 0.5 * (r - l)
        y = func(x, *args)
        if abs(val - y) <= tol:
            return x
        if val < y:
            r = x
        else:
            l = x
        i += 1
        if i > 500:
            return None

# Main function
def main():
    print("TANK VOLUME FRACTION FROM DIPSTICK READING\n")
    print("A - horizontal cylindrical tank")
    print("B - spherical tank")
    print("C - elliptical tank")
    print("D - vertical cartouche")
    print("E - horizontal cartouche")
    print("F - bucket (conic frustum)")
    print("G - barrel (elliptical sides)")
    print("H - horizontal cylindrical tank with hemispherical ends")
    print("I - horizontal cylindrical tank with dished ends")

    op = input("(A-I) ? ").lower()

    if op not in "abcdefghi":
        print("NOT A VALID OPTION")
        return

    if op in "abcfgh":
        d = float(input("Tank diameter: "))
        r = d / 2.0

    if op == "c":
        a = float(input("Tank horizontal dimension: "))
        b = float(input("Tank vertical dimension: "))
        d = b
        a *= 0.5
        b *= 0.5

    if op in "de":
        a = float(input("Tank horizontal dimension: "))
        b = float(input("Tank vertical dimension: "))
        d = b
        r = a / 2.0
        l = a - b

    if op == "i":
        d = float(input("Tank diameter: "))
        l1 = float(input("(Maximum) Tank length over ends: "))
        l2 = float(input("Length of cylindrical portion of tank: "))
        r = d / 2.0
        hdish = 0.5 * (l1 - l2)
        vd = PI * hdish * (3 * r * r + hdish * hdish) / 6.0
        tvol = PI * r * r * l2 + 2 * vd
        print(f"Total volume of tank = {tvol:.3f}")

    h = float(input("Wetted dipstick length: "))

    if h < 0 or h > d:
        print("INPUT MAKES NO SENSE. Try again.")
        return

    if op == "a":
        f = fcyl(h, r)
    elif op == "b":
        f = fspher(h, r)
    elif op == "c":
        f = fellip(h, a, b)
    elif op in "de":
        f = fvcart(h, a, b, r, l)
    elif op == "f":
        db = float(input("Diameter of bucket big end: "))
        ds = float(input("Diameter of bucket small end: "))
        hb = float(input("Vertical height of bucket: "))
        rb = db / 2.0
        rs = ds / 2.0
        t = rs * rs + rs * rb + rb * rb
        tvol = PI * hb * t / 3.0
        print(f"Total volume of bucket = {tvol:.3f}")
        f = fbuck(h, hb, rb, rs)
    elif op == "g":
        db = float(input("Diameter of barrel at middle: "))
        ds = float(input("Diameter of barrel at end(s): "))
        hb = float(input("Vertical height of barrel: "))
        rb = db / 2.0
        rs = ds / 2.0
        tvol = PI * hb * (2 * rb * rb + rs * rs) / 3.0
        print(f"Total volume of barrel = {tvol:.3f}")
        f = fbarrel(h, hb, rb, rs)
    elif op == "h":
        tvol = PI * r * r * (l - d + 4 * r / 3.0)
        print(f"Total volume of tank = {tvol:.3f}")
        f = fhcyl(h, r, a, d)
    elif op == "i":
        tvol = PI * r * r * l2 + 2 * vd
        print(f"Total volume of tank = {tvol:.3f}")
        f = fdcyl(h, r, l1, l2)

    print(f"\nTank has {100 * f:.2f}% of its full capacity remaining\n")

    print("Calibration of dip stick as a function of tank volume.\n")

    inc = float(input("Percentage increment of tank volume: "))

    if inc <= 0.0 or inc > 100.0:
        print("INPUT MAKES NO SENSE. Try again.")
        return

    for f in range(int(inc), int(100 - inc) + 1, int(inc)):
        h = binsearch(0.0, d, 0.01 * f, 0.00001, fcyl, r)
        print(f"Tank volume = {f:.2f}%, stick wetted length = {h:.2f}")
    
    print(f"Tank volume = 100.00%, stick wetted length = {d:.2f}")

if __name__ == "__main__":
    main()
