# li = [10,12,13,15,14]
#
# def even_extraction(li):
#     even = []
#
#     for i in li:
#         if i%2 == 0:
#             even.append(i)
#     return even
# print(even_extraction(li))
#
# #syntax - filter(functional cond , collection)
#
# li = [10,11,12,13,14,15]
# data = list(filter(lambda i:i%2==0,li))

# li = [10,'ty',19,'wo']
# data = filter(lambda i:type(i)==str,li)
# print(data)

#MAP - it is powerful fun of python, it is modify the collectionl of element
#map(functional condition, collection)

# li = [10000,20000,15000,9000]
# data = list(map(lambda i:i+2000,li))
# print(data)
#REDUCE
from functools import reduce
#reduce(functional condition ,collection)
li = [10000,20000,15000,9000]
data = reduce(lambda a,b:a+b,li)
print(data)