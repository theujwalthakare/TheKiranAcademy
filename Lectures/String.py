# 05 - 06 - 2025
# string  methods, Logical Questions
from itertools import count
s = "Instagram"
count = 0
# print("start of loop")
# for var in s:
#     print()
#     pass
# print("end of loop")

# chech the frequency of character b in the given sting 
name = "My name is Ujwal Thakare "
c =0
vowels = 'aeiou'
for i in range(0,len(name)):
    print(i,"=",name[i])
    # count vowels in name 
    if name[i] == 'a' or name[i] == 'e' or name[i] == 'i' or name[i] == 'o' or name[i] == 'u':
        c += 1
print("the count of vowels in name is  = ", c)
co = 0
for i in name.lower():
    if i in vowels:
        co += 1
print("the count of vowels in name is  = ", c)
# print in reverse the string name 
for i in range(len(name)-1,-1,-1):
    pass

    
   
# range(0,5) -> 0 to 5 
# range(0,5,2) -> third parameter is step size 
# for i in range(0,len(name)):
#     print(i,"--->", name[i])
#     if name[i] == 'b':
#         count += 1
# print("the frequency of b is =  ", count)
        

#home work : string methods lower, upper, startwith, endswith, isalpha(), isalnum(),..etc
