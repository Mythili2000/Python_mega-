def findpassorfail(mark):
    if mark < 35:
        print("The mark",mark,"is fail")
    elif mark >= 35 and mark < 100:
        print("The mark",mark,"is pass")
    else:
        print("The mark is for out of 100")

value = int(input("Enter your mark:"))
findpassorfail(value)

