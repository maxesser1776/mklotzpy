import math

# Global constants
DPR = 180 / math.pi
PI = math.pi
TWOPI = 2 * PI

# Utility functions
def SQR(a):
    return a * a

def RSS2(a, b):
    return math.sqrt(SQR(a) + SQR(b))

# Cam design
def cam():
    # User input
    ctype = int(input("TYPE OF FOLLOWER MOTION (1-4): "))
    rtype = int(input("TYPE OF CAM FOLLOWER (1-2): "))

    if rtype == 2:
        rroll = float(input("Radius of roller: "))
    else:
        rroll = 0.0

    rbase = float(input("Base circle radius: "))
    risea = 0.0
    rised = 0.0
    betaa = 0.0
    betal = 0.0
    beta = float(input("Cam rotation angle (degrees): "))
    astep = float(input("Angular step size for constructing cam (degrees): "))

    # Initialize variables
    xmin, xmax, ymin, ymax = -640, 640, -480, 480
    wx, wy = xmax - xmin, ymax - ymin

    # Open output file
    with open("CAM.DAT", "w") as fp:
        fp.write("CAM DESIGN\n")
        fp.write(f"TYPE OF FOLLOWER MOTION: {ctype}\n")
        fp.write(f"TYPE OF CAM FOLLOWER: {rtype}\n")
        if rtype == 2:
            fp.write(f"Follower Roller Radius: {rroll}\n")
        fp.write(f"Base Circle Radius: {rbase}\n")
        fp.write(f"Cam Rotation Angle: {beta} degrees\n")
        fp.write("\nAngle is measured from highest point of cam.\n")
        fp.write("Radius & x,y coordinates measured from center of cam rotation.\n")
        fp.write("\n     Angle      Radius     X-coord     Y-coord\n")

        # Calculate cam parameters and draw cam
        pamax = 0.0  # Maximum pressure angle
        scale = 200 / (rbase + risea)  # Scales drawing
        rbs = rbase * scale  # Base radius in pixels
        ocam = scale * (2 * rbase + risea)  # Overall length of cam in pixels
        rob = risea / (beta * DPR)
        xmin = -(320 - 0.5 * ocam + rbs)
        xmax = 640 + xmin
        ymin = -240
        ymax = 240

        # Draw base circle
        print(f"Drawing base circle with radius: {rbase}")
        print("Press Enter to continue...")
        input()

        # Draw cam profile
        xl, yl = rbs * math.cos(beta), rbs * math.sin(beta)
        print(f"Drawing cam profile from (0, 0) to ({xl}, {yl})")
        print("Press Enter to continue...")
        input()
        xt, yt = xmin, ymin
        vt = ymin

        for ang in range(int(beta), -1, -int(astep)):
            theta = beta - ang
            tob = theta / beta

            if ctype == 1:
                ba = 120.0 / (1.0 + 2.0 * (risea + rised) / betal)
                th = theta * DPR

                if theta <= betaa:
                    d = risea * (th / ba) ** 2
                    vc = 2.0 * risea * th / (ba ** 2)
                    ac = 2.0 * risea / (ba ** 2)
                elif theta >= (betaa + betal):
                    th = (theta - betaa - betal) * DPR
                    d = risea + betal * (theta - betaa) / betal
                    vc = betal / betal
                    ac = 0
                else:
                    d = risea + betal * (theta - betaa) / betal
                    vc = betal / betal
                    ac = 0

                vmax = betal / betal
            else:
                if tob <= 0.5:
                    d = 2.0 * risea * tob ** 2
                    vc = 4.0 * rob * tob
                    ac = 4.0 * rob / beta
                else:
                    d = risea * (1.0 - 2.0 * (1.0 - tob) ** 2)
                    vc = 4.0 * rob * (1.0 - tob)
                    ac = -4.0 * rob / beta

                vmax = 2.0 * rob

            rcam = math.sqrt((rbase + d + rroll) ** 2 - rroll ** 2)
            pcam = math.atan(vc / (rbase + d + rroll))
            if pcam > pamax:
                pamax = pcam
                vcmax = vc
                smax = d

            tcam = ang * DPR - pcam
            xcam, ycam = rcam * math.cos(tcam), rcam * math.sin(tcam)
            x = xcam
            y = ycam

            xl, yl = x, y

            xp = theta * 640 / beta + xmin
            yp = d * 480 / risea + ymin
            vp = vc * 480 / vmax + ymin
            ap = ac * 240 / beta

            xt = xp
            yt = yp
            vt = vp
            at = ap

            fp.write(f"{ang:10.4f}  {rcam:10.4f}  {xcam:10.4f}  {ycam:10.4f}\n")

    print(f"The maximum pressure angle was {pamax * DPR:.4f} degrees")
    print("\nMaximum pressure angle should be less than 35 degrees to limit side thrust on the follower.")
    print("Pressure angle can be adjusted by modifying the base radius.")

if __name__ == "__main__":
    cam()
