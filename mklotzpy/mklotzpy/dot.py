import math

# Constants
RPD = math.pi / 180.0
DPR = 180.0 / math.pi

# Function to calculate depth of thread
def thread_depth():
    ta = float(input("Threads angle (degrees): "))
    tpi = float(input("Threads per inch: "))
    rang = float(input("Compound rest angle (degrees): "))

    cang = math.cos(math.radians(rang))
    pitch = 1.0 / tpi
    h = 0.5 * pitch / math.tan(math.radians(0.5 * ta))  # Dot sharp crest to sharp root
    dotfcfr = 0.625 * h  # Dot flat crest to flat root
    dotscfr = 0.75 * h   # Dot sharp crest to flat root
    dotfcsr = 0.875 * h  # Dot flat crest to sharp root
    undercut = 0.25 * h  # Undercut below nominal diameter for class 2A and 2B threads
    dotscsr = 2.0 * h     # Double dot sharp crest to sharp root

    print("\nDEPTH OF THREAD CALCULATIONS\n")
    print(f"Thread angle = {ta:.2f} degrees")
    print(f"Threads per inch = {tpi:.1f} (pitch = {pitch:.5f} in/thread)")
    print(f"Compound feed at compound angle = {rang:.1f} degrees\n")

    print(f"(A) Dot sharp crest - sharp root = {dotscsr:.5f} in ({dotscsr / cang:.5f} in)")
    print(f"(B) Dot flat  crest - flat  root = {dotfcfr:.5f} in ({dotfcfr / cang:.5f} in)")
    print(f"(C) Dot sharp crest - flat  root = {dotscfr:.5f} in ({dotscfr / cang:.5f} in)")
    print(f"(D) Dot flat  crest - sharp root = {dotfcsr:.5f} in ({dotfcsr / cang:.5f} in)")
    
    z = (3.0 / 16.0) * pitch / math.tan(math.radians(30.0))  # Distance of pitch line below p/8 flat
    print(f"\nFor American National (60 deg) thread form, subtract {2.0 * z:.4f} in from")
    print("major diameter (assumes p/8 flat on crest) to obtain pitch diameter")
    
    fracp, intp = math.modf(tpi)
    if fracp:
        print("Use any odd-numbered line on threading dial")
    else:
        if int(intp) % 2:
            print("Use any numbered line on threading dial")
        else:
            print("Use any line on threading dial")

if __name__ == "__main__":
    thread_depth()
