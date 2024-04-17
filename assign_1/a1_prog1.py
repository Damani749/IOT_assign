#Write a Python Program find an area of a rectangle and perimeter of the rectangle.

len = float(input("Enter the length of the Rectangel.\n"))
bre = float(input ("Enter the breadth of the Rectangle.\n"))

area = len * bre;
peri = 2 * (len + bre)

def area_fun(len, bre):
    print(f"Area of Rectangle: {area}")

def peri_fun(len, bre):
    print(f"Perimeter of Rectangle: {peri}")

area_fun(len, bre)
peri_fun(len, bre)