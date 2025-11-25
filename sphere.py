# inspiration code for Python Unit Testing Project
import math
def surfaceArea(rad):
    return 4 * math.pi * (rad ** 2) 

def volume(rad):
    import math
    return (4/3) * math.pi * (rad ** 3)

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))
    
    print("\nThe Volume of a Sphere = ", volume(radius))
    print("\nThe Surface Area of a Sphere = ",surfaceArea(radius))

if __name__ == '__main__':
    prompt()
