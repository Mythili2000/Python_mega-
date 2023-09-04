def add():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15]
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum
result = add()
print(result)
