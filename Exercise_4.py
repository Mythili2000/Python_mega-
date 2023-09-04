# count the number of even and odd
e_count = 0
o_count = 0
for i in range(1,11):
    if i % 2 == 0:
        count = e_count + 1
    else:
        count = o_count + 1
print("count of even is:",e_count)
print("count of odd is:",o_count)