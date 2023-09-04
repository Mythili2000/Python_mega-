a = []
print("Enter 10 numbers:")
for i in range(5):
    num = int(input("Enter num "+str(i+1)+" = " ))
    a.append(num)
print("The 10 numbers are:",a)

sum = 0
for i in a:
    sum = sum + i
Average = sum/5
print("The average is",Average)
print("The total sum is:",sum)