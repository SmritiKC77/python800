l1 = [2,3,5,6]
total = 0
index = 0
mean = 0
n = len(l1)
while index <len(l1):
    item = l1[index]

    total = total + item
    index = index +1
mean = total/n
print("Mean = ",mean)
