# one of the pillars of OOP
# -> Same name entity behaves differently at different time is called polymorphism
# -> poly -> many 
# -> morphs -> forms
# -> In Python there are two type of polymorphism
#       1. Overloading
#            -> operator overloading
        #    for static programming lang there are two overloading
        #    - Method overloading 
        #    - Constructor overloading
#       2. Overridng
#            -> method overriding
            #    - redefining parent class method into child class method is called method overriding 

# class Student():
#     def __init__(self,r):
#         self.roll = r
#     def __init__(self,r,n):
#         self.roll = r
#         self.name = n
#     def __init__(self,r,n,m):
#         self.roll = r
#         self.name = n
#         self.marks = m

#     def m1(self,a):
#         self.a = a
#         print(a)
#     def m1(self,b,s):
#          self.b =b
#          self.s=s
#          print(b,s)

# # s1 =Student(1)
# # s2 =Student(1,"ujwal")
# # s3 = Student(2,"ujwal",20)
# # s3.m1(12,'dasd')
# class book:
#     def __init__(self,name,p):
#         self.bookname = name
#         self.price = p
#     def __add__(self,other):
#         return self.price + other.price
        
    
# b1= book("core python",200)
# b2 =book("Adv python",400)
# print(b1 + b2)
# print(b1-b2)  HW
# print(b1*b2)  HW

class A():
    name = "ujwal"
    
    @classmethod
    def M1(cls):
       cls.name
       print("class A -> calling M1 method")
    
    @staticmethod
    def M2(arg):
        print(arg)
        
    
    
class B(A):
    name ="samir"
    @classmethod
    def M1(cls):
        cls.name
        print("class B -> calling M2 method")
    @staticmethod
    def M2(arg):
        print(arg)    
           
           
            
child = B()
child.M1()
print(child.name)
child.M2(123)

# who is the parent of all class -> object class
# operator overload karke dekhna hai ?
# find names of object class methods python ? 
# what is use of __str__() method ? // it decide representation of string 
