
# # Exactly same as list only difference is List is Mutable and tuple is immutable
# # Tuple is written in () parenthesis

    
# t = ("ujwal", 786, True, 35.88)
# print(t)
# print(type(t))
# print(id(t))

# # t = ("ujwal",)
# # print(type(t),t)

# # s = ["ujwal",]
# # print(type(s), s)
# for data in t:
#     print(data)

# for i in range(len(t)):
#     print(i ," -- >",t[i])

# l = list(t) # typecast tuple into list
# l.append("thakare")
# print(l)
# t = tuple(l) # typecast lists into tuple
# print(t)


t = (5,2,9,5,5,1,8,2)
print(t)
s = set(t)
print(s)
t1 = tuple(s)
print("Total student present in the class  :",len(t1))
print("roll number of present studnet is :",t1)
for i in range(1,11):
    if i not in t1:
        print("roll number of absent student is :", i)


