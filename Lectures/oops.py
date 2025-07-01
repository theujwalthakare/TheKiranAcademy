# class student:
#     name = "ujwal"
#     age = 21
    

# obj = student()
# print(type(obj))


# Inheritence 
# -> we can not do polymorphism (Method Overriding) without inheritence
#   Types of inheritence
#   1. Simple / Single
#   2. Multilevel 
#   3. Multiple
#   4. Hierachical
#   5. Hibrid
#   6. Cyclic (Not supported in any language)                 

#   1. Simple / Single
#   -> one parent and one child kind of inheritence is called single inheritence 
# class Parent():
#     def property(self):
#         l = ['cash','gold','car','land']
#         print(l)

# class Child(Parent):
#     def m1(self):
#         print("m1 method from child class")
     
# h = Child()
# h.m1()
# h.property()

#   2. Multilevel 
#       -> Inheritence in levels is called multilevel 


# class A:
#     # print("class A call")
#     def M1(self):
#         print("A class")
# class B(A):
#     # print("Class B call")
#     def M2(self):
#         print("B class")
# class C(B):
#     print("class C call")
#     def M3(slef):
#         print("C class")
    
# c1 = C()
# c1.M3()
# c1.M2()
# c1.M1()

# a = A()
# a.M1

# b = B()
# b.M1()
# b.M2()

# Multiple Inheritence
# class N:
#     def M2(self):
#         print("N of M2")
# class A(N):
#     # print("class A call")
#     def M1(self):
#         print("A class")
# class B:
#     # print("Class B call")
#     def M2(self):
#         print("B class")
# class C(B,A):                   # MRO(method resolution order)
#     print("class C call")
#     def M3(slef):
#         print("C class")
    
# c1 = C()
# # c1.M3()
# c1.M2()
# # c1.M1()

# 4. Hierarchical Inheritence 
#  -> One Parent and Multiple child 

# class A():
#     # print("class A call")
#     def M1(self):
#         print("A class")
# class B(A):
#     # print("Class B call")
#     def M2(self):
#         print("B class")
# class C(A):                   # MRO(method resolution order)
#     # print("class C call")
#     def M3(slef):
#         print("C class")
# class D(A):
#     def M4(self):
#         print("D class")
# c = C()
# c.M1()

# b =B()
# b.M1()

# d = D()
# d.M1()


#   5. Hibrid
#    ->

# HW -> Higher order functions
class player : # use incapsulation
    def __init__(self,jn,n,run, wicket, tname):
        pass

    # getter & setter
    
p1 =player(42,"rohit",6500,29,"RCB")
p2 =player()
miteam = []
miteam.append(p1,p2)

for p in miteam :
    print("")
    
    
# 7 july shedule home work
