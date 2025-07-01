# def Addnum(x,y):
#     sum = x + y
#     print("Addition = ",sum)

# # Addnum(12,45)
# Addnum(int(input()),int(input()))

# def table():
#     num = int(input("Enter number "))
#     # sum = 8+9
#     for i in range(1,11):
#         print(num*i)
#     return num
#     # return sum

# table()

# def maxnumber(n1,n2):
#     if(n1 > n2):
#         return {n1,n2,"wd"}
#     else:
#         return n2,n1,"dwd"
# max = maxnumber(30,20)
# a,b,c = max
# print(a, b, c)
# print(max)
# print(type(max))
# a=10
# b=20
# c=30
# d=40
# bag = a,b,c,d
# print(bag)
# print(type(bag))

# Types of Arguments in function
# 1. Positional argument 
# 2. Keyword Argument -> here we can pass arg in any position
# 3. Default Argument -> It is use to pass some default value to function # if in your funcation default parameter put it into last arg in keyword
# 4. Arbitary Argumen (Variable length Arguments)-> 
#               def funname(*args):                                    
#                       body of function 
        # -> Positional Arbitary : position/sequence matters
        # -> Key word Arbitary : position / order sequence dosent matter
# example of Positional Arbitary
# def addnum(*ujwal):
#     print(type(ujwal))
#     print(ujwal)
#     res = sum(ujwal)
#     print(res)
# addnum(1,2,13,4,2)
# addnum(2,5,3)

# def submit(**ujwal):
#     print(type(ujwal))
#     print(ujwal)

# submit(name="ujwal",roll=101,cname="KVN",marks=86,subject="maths")



# numbers=[5,'A',' ',1,2]
# print(any(numbers))
# print(all(numbers))

word =['apple' , 'banssana' ,'orange', 'cherry']
sorted_word = sorted(word, key=len)
print(sorted_word)