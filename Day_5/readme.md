# to check how pop and remove method use in LIST as well in TUPLE and what its return type  
- Program is:
##     
    L1 = [1, 2, 3, 4, 5]
    L2 = ["ujwal","yadnyesh","rahul","manish","kumar"]
    L3 = [True, False, True, False, True]

    print("Before changes ->",L1) # befor 
    print("type of element is : ", type(L1[2]),"Element at position index 2 is :->",L1.pop(2)) # remove the element from list by index
    print("After Makning changes ->",L1)
    print(type(L2.pop(2))) # remove the element from list by index and can not return by the value
    
    print("Before changes ->", L2) # befor
    print(L2.remove("manish")) # remove the element from list by value and can not return by the index
    print("After Makning changes ->", L2)
    print(type(L3.remove(True))) # it will only check the first occurence 
    print(L3)

## output of the following code is :
    Before changes -> [1, 2, 3, 4, 5]
    type of element is :  <class 'int'> Element at position index 2 is :-> 3
    After Makning changes -> [1, 2, 4, 5]
    <class 'str'>
    Before changes -> ['ujwal', 'yadnyesh', 'manish', 'kumar']
    None
    After Makning changes -> ['ujwal', 'yadnyesh', 'kumar']
    [False, True, False, True]
    <class 'tuple'>
    <built-in method index of tuple object at 0x000001F2DA577700>
    5 is repeated in tuple -> 2 Times
    (1, 2, 3, 4, 5, 54.65, 5)