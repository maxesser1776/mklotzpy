import math

def main():
    print("BOLTCIRCLE COMPUTATIONS\n")

    # Input parameters
    nh = int(input("Number of holes: "))
    rc = float(input("Radius of bolt cirlce (in): "))
    dh = float(input("Diameter of bolt holes (in): "))
    a0_deg = float(input("Angular offset of first hole (deg): "))
    x0 = float(input("X offset of bolt circle center: "))
    y0 = float(input("Y offset of bolt circle center: "))

    sp = 360.0 / nh 
    space = 2.0 * rc * math.sin(math.radians(0.5 * sp)) - dh
    if space < 0.0:
        print("\nWARNING: HOLES WILL OVERLAP !")

    ofile ="BOLTCIRC.dat"
    with open(ofile, "wt") as fp: 
        fp.write("Boltcirlce specifications:\n")
        fp.write(f"Radius of bolt circle = {rc:.4f}\n")
        fp.write(f"Bolt hole diameter = {dh:.4f}\n")
        fp.write(f"Spacing between hole edges = {space:.4f}\n")
        fp.write(f"Angular offset of first hole = {a0_deg:.4f}\n")
        fp.write(f"X offset of bolt circle center = {x0:.4f}\n")
        fp.write(f"Y offset of bolt circle center = {y0:.4f}\n")
        fp.write("HOLE      ANGLE     X-COORD     Y-COORD\n\n")
                 
        for i in range(nh):
            ang = a0_deg + i * sp
            x = rc * math.cos(math.radians(ang)) + x0
            y = rc * math.sin(math.radians(ang)) + y0
            fp.write(f"{i + 1:4d}   {ang:10.4f}   {x:10.4f}   {y:10.4f}\n")
    print(f"\nYour data is on: {ofile}")

if __name__ == "__main__":
    main()
                 
                 