# # addition fun
# def Addnum(x,y):
#     sum1 = x+y
#     # print("sum of ",x," + ",y ," = ",sum1)
#     # return sum1
#     #  always use return in last line of function

# print("We are calling Function")
# s1=Addnum(19,10)
# print(s1)
# print("after Calling Function")

# # def Subnum():
# #     x =int(input("x = "))
# #     y =int(input("y = "))
# #     print("substraction of {x} - {y} is ",x-y)

# # Subnum()

# def listprint(food):
#     for x in food:
#         print(x)
#     print(type(food))
#     print(food)
# fruit=["mango","orange","grape","apple"]
# listprint(fruit)

# def tupleprint(num):
#     for i in num:
#         print(i)
#     print(type(num))
#     print(num)
# numeric = (12,12,32,443,54,54)
# tupleprint(numeric)

# def setprint(letter):
#     for i in letter:
#         print(i)
#         print(type(i))
#     print(type(letter))
#     print(letter)
# letr = set()
# letr = {23,24,42,22}
# letr.add(12)

# print(type(letr))
# setprint(letr)

# def dictprint(first):
#     for x,y in first.items():
#       print(y)
#     print(type(first))
    
# fir = {1:"ujwal",2:"yadnyesh",3:"rahul"}
# print(type(fir))
# dictprint(fir)

# def stringprint(string ,int):
#     print(string,int)
#     print(type(string))

# stringprint('this is me live in india',23)

# going to build calculator

def add(n1,n2):
    sum = n1 + n2
    return sum
def sub(n1,n2):
    sub = n1 -n2
    return sub
def div(n1,n2):
    div = n1/n2
    return div
def mul(n1,n2):
    mul = n1*n2
    return mul
def avg(n1,n2):
    add(n1,n2)
    avg = sum / 2 # avg = n1 + n2 / 2
    return avg
def mod(n1,n2):
    mod  = n1 % n2
    return mod

print("Welcome to calculator")
