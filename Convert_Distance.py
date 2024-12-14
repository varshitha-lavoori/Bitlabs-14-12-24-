def distance():
    dist=float(input("Enter the distance in feet:"))
    print("Distance in feet:",dist)
    inch=(dist*12)
    print("Distance in inches:",inch)
    yards=dist/3
    print("Distance in yards:",yards)
    miles=dist/5280;
    print("Distance in miles:",miles)
distance()