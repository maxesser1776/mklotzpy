import math

def main():
    print("BUCKET CALCULATIONS\n")

    # Input parameters
    db = float(input("Diameter of bucket big end (in): "))
    ds = float(input("Diameter of bucket small end (in): "))
    sh = float(input("Slant height of bucket (in): "))
    n = int(input("Divide volume into how many parts: "))

    rb = 0.5 * db
    rs = 0.5 * ds
    theta = math.degrees(math.asin((rb - rs) / sh))
    h = sh * math.cos(math.radians(theta))
    t = rs ** 2 + rs * rb + rb ** 2
    vol = (math.pi * h * t) / 3.0

    print("\nTotal volume of bucket = (:.3f)".format(vol))

    eps = 0.001 * vol
    dh = 0.001 * h
    for i in range(1, n + 1):
        vi = i * vol
        hi = i * h / n
        k = 0 # Safety valve
        while True:
            ri = rs + hi * (rb - rs) / h
            t = ri ** 2 + rs * ri + rs ** 2
            ve = (math.pi * hi * t) / 3.0 
            k += 1
            if k > 500:
                print("Iteration error")
                quit()
            if abs(vi - ve) < eps:
                break
            hi += dh * ((vi - ve) / abs(vi - ve))

        shi = hi / math.cos(math.radians(theta))
        print("Slant height for {}/{} of total volume = {:.3f}".format(i, n, shi))

if __name__ == "__main__":
    main()