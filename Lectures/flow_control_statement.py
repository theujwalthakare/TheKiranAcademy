# 13/06/2025 Flow Control Statement
# 1. Conditional statement
#      - if , if-else, else
# 2. Iterative Statement
#      - for loop, while
# 3. Transfer Control statement
    #  - pass, continue , break
    
# 1. Conditional Statement :
# -> To check half condition we can use if statement (always use those operators which gives o/p in boolean)
# -> To check one complete condition we use if - else statement
# -> To check multiple condition we use elif

# Task : three Student in a class with some ages .
# jay =23, viru=22, gabbar =24
# # WAP to find who is older
# jay = 24
# viru = 24
# gabbar = 24
# if jay >0 and viru >0 and gabbar >0 :
#     if jay > viru and jay > gabbar:
#          print("Jay is older")
#     elif viru > gabbar and viru > jay:
#         print("Viru is older")
#     elif gabbar > jay and gabbar > viru:
#         print("Gabbar is older")
#     elif jay == gabbar and viru == jay:
#         print("all has same age ")
#     elif jay == viru:
#         print("jay and viru has same age ")
#     elif jay == gabbar:
#         print("jay and gabbar has same age ")
# else:
#     print("invalid credential ")
    
# Task 2:
# you have a given number eg n = 9 WAP To check following condition
# 1. num divisible by 3 print "fizz"
# 2. num divisible by 5 print "buzz"
# 3. num divisible by 3 and 5 print "fizzbuzz"
# n= int(input("Enter number"))
# if n%3 ==0 and n%5 ==0:
#      print("fizzbuzz")
# elif n%3==0:
#     print("fizz")
# elif n%5==0:
#     print("buzz")
# else:
#     ("invalid Credintial")


#  Iterative Statement 
#   -for loop-> If we know number of iteration in advance then use " for loop "


# print("1 \n 2 \n 3 \n 4 \n 5")

# print("Table of 5")
# for i in range(1,11):
#     i =5*i
#     print(i)
# n=int(input("Enter num"))
# for i in range(1,11):
#     i=n*i
#     print(i)

# for i in range(1,31):
#     if i%3==0 and i%5==0:
#         print("fizzbuzz")
#     elif i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     else:
#         print(i)
for i in range(100,0,-1):
    print(i)
