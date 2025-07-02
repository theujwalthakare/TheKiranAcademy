class A():
    def M1(self):
        print("class A -> calling M1 method")
    
class B(A):
    def M2(self):
        print("class B -> calling M2 method")
class E(B):
    def M5(self):
        print("class E -> calling M5 method")
        # make obj of E
class C(A):
     def M3(self):
         print("class C -> calling M3 method")
class D():
     def M4(self):
         print("class D -> calling M4 method")
class F(C,D):
    def M6(self):
        print("class F -> calling M6 method")
        
jay = E() #object of class E
viru = F() #object of class F
print("accesing M1 method from class A using E class object")
jay.M1()   #method M1 from class A
viru.M4()  # method M4 from class D 
jay.M2()
viru.M3()

jay.M5() # calling M5 method from class E 
viru.M6() # calling M6 method from class F 


