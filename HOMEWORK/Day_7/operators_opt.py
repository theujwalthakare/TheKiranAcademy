# #------------------ Home Work   -------------------
# # addition, substraction, multiplication of all data type except string and number 
# # also try combination of data for ex.:-> ( string * num , str * float )

a = 12
b = 3
c = "ujwal"
d = "thakare"
e = 12.5
t = True
f = False
# addition
print("int - int = ",a+b)

# print(a+c) //  Unsupported operand type(s) for +: 'int' and 'str'

print("str + str = ",c+d)
print("int + float = ",a+e)

# print(e+c) // TypeError: unsupported operand type(s) for +: 'float' and 'str'

print("bool + bool = ",t+f)

# substraction
print("int - int = ",a-b)
print("int - int = ",b-a)

# print(a-c) // TypeError: unsupported operand type(s) for -: 'int' and 'str'

print("int - float = ",a-e)
# print(c-d) // TypeError: unsupported operand type(s) for -: 'str' and 'str'

# print(c-e) TypeError: unsupported operand type(s) for -: 'str' and 'float'

print("bool - bool = ",f - t) 

# multiplication
print("int * int = ", a*b)
print("int * float = ", a*e)
print("str * int = ", c*b)
print("bool * bool = ", t*f)
print("bool * int = ", t*b)
print("bool * float = ", t*e)
print("int * bool = ", a*f)
print("float * bool = ", e*f)
print("float * int = ", e*b)
print("float * float = ", e*e)
# print("float * str = ", e*d) // TypeError: can't multiply sequence by non-int of type 'float'
# print("str * float = ", c*e)  // TypeError: can't multiply sequence by non-int of type 'float'

print("str * bool = ", c*f)
# print("str * str = ", c*d) // TypeError: can't multiply sequence by non-int of type 'str'

# create a list, set, tuple, dict, string and perform all the operations on it
l = [1,2,3,4,5,6,7,8,9,10]
s = {1,2,3,4,5,6,7,8,9,10}
t = (1,2,3,4,5,6,7,8,9,10)
d = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
str = "saibuyguybuybubv"
# try combination of data to calculate addition, multiplication, substraction
print("list + list = ", l+l)
# print("set + set = ", s+s)
print("tuple + tuple = ", t+t)
# print("dict + dict = ", d+d)
print("str + str = ", str+str)
# print("list + int = ", l+a)
# print("set + int = ", s+a)
# print("tuple + int = ", t+a)
# print("dict + int = ", d+a)
# print(l + d)





