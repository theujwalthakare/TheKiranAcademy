# set is mutable , Heterogenious collection of immutable elements where insertion order is NOT maintained and duplicates are NOT allowed. 

# major advantage of set is it removes duplicates and maintains unique elements only

# s = set()
# print(s)
# print(type(s))
# print(id(s))
# s.add(10)
# s.add(12)
# print(s)

l1 =[10,21,65,50]
l2 = ["ujwal","ram","hello"]
t = (10,20,30,40)
s = {9,8,5,6}
s1 = {98,25,65,6}
print(s.union(s1))
# s.add(l1)
# print(s2)

# l1.insert(2,l2)
# print(l1)

# print(l1[2][1][0])

# l1.insert(2, t)
# print(l1)

# l1.insert(2, s)
# print(l1)

# print(l1[2])

# for data in l1[2]:
#     print(data)

# print(t)
# print(t[4][0]) # 10
# print(t[5][0]) # ujwal
# print(t[6])

# m = list(t)
# m.append(l1)
# print(m)

# t = tuple(m)
# print(t)

# Frozen Set :- It is immutable , Heterogenious collection of immutable elements where insertion order is NOT maintained and duplicates are NOT allowed. 

fs = frozenset(s)
print(fs)


