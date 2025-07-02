# make a simpl
L1 = [1, 2, 3, 4, 5]
L2 = ["ujwal","yadnyesh","rahul","manish","kumar"]
L3 = [True, False, True, False, True]

# POP method

print("Before changes ->",L1) # befor 
print("type of element is : ", type(L1[2]),"Element at position index 2 is :->",L1.pop(2)) # remove the element from list by index
print("After Makning changes ->",L1)
print(type(L2[2]),L2.pop(2)) # remove the element from list by index and can not return by the value
print(L2)
print(type(L3[2]), L3.pop(2)) # remove the element from list by index and can not return by the value
print(L3)
# you can also use empty pop() it will delete last element from list
L5=[28,29,30,31]
print(L5)
print(L5.pop()) # it will delete last element from list
print(L5)

# Remove method

print("Before changes ->", L2) # befor
print(L2.remove("manish")) # remove the element from list by value and can not return by the index
print("After Makning changes ->", L2)
print(type(L3[True]),L3.remove(True)) # it will only check the first occurence 
print(L3)
# check methods like .pop(index/value ? what is the parameter), .remove(value/index ??) also check return type

# print(type(L3.append(54)))
# print(L3)
#
T1 = (1, 2, 3, 4, 5,54.65,5)
T2 = ("ujwal","yadnyesh","rahul","manish","kumar")
T3 = (True, False, True, False, True)
print(type(T1))
print(T1.index)
print("5 is repeated in tuple ->",T1.count(5),"Times") # it will count the number of times element occur in tuple 
print(T1)





