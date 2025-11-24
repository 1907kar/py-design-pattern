# Problem: find the index of the nos, when adding them both it is equal to the target

# Type - 1
target = 9
li = [2, 7, 11, 15]

# Type -2
# target = 10
# li = [3, 4, 7, 1]

# Traditional iteration
# li_len = len(li)
# li_found = []
# for x in li:
#     for y in range(0, li_len):
#         n = li[y]
#         if li.index(x) != y:
#             print(x, n)
#             if x + n == target:
#                 li_found.append([li.index(x), li.index(n)])
#                 break
# print(li_found)

# using complementary logic
for index, num in enumerate(li):
    x = target - num
    if x in li:
        print(li.index(num), li.index(x))
        break