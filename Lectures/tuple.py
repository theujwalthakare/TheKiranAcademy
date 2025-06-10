
# Exactly same as list only difference is List is Mutable and tuple is immutable
# Tuple is written in () parenthesis

    
t = ("ujwal", 786, True, 35.88)
print(t)
print(type(t))
print(id(t))

# t = ("ujwal",)
# print(type(t),t)

# s = ["ujwal",]
# print(type(s), s)
for data in t:
    print(data)

for i in range(len(t)):
    print(i ," -- >",t[i])

l = list(t) # typecast tuple into list
l.append("thakare")
print(l)
t = tuple(l) # typecast lists into tuple
print(t)