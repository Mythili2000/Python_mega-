a = []
sum = 0
number = int(input("Enter a number:"))
for i in range(1,1+number):
    sum = sum + i
    a.append(i)
print("The sum number is",sum)
print("The natural numbers of",number,"is:",a)