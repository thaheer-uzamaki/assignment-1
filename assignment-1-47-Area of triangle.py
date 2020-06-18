import math
ch=int(input("Enter 1 if you have base and height of triangle\nEnter 2 if you have sides of the triangle\n"))
if ch==1:
    base=float(input("Enter the base of triangle: - "))
    height=float(input("Enter the height of triangle: - "))
    area=0.5*base*height
    print("Area of the triangle: - {}".format(area))
elif ch==2:
    s1=float(input("Enter the side1 of triangle: - "))
    s2=float(input("Enter the side2 of triangle: - "))
    s3=float(input("Enter the side3 of triangle: - "))
    s=(s1+s2+s3)/2
    area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    print("Area of the triangle: - {}".format(area))
else:
    print("Wrong input")
