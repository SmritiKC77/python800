data = [[5,3],[22,11,1],[0,4],[2,3,4,5,6]]
# Each list item ko total naya list ma chaiyo
print(data[0])
one_list = [5,3]
total = 0
for item in one_list:
    total = total + item
print("total",total)

for one_list in data:
    total = 0
    for item in one_list:
        total = total + item
    print(total)