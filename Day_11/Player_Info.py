# class PlayerInfo():
#     # 
#     def __init__(self,JN,name,runs,wickets,team_name):
#         self.JN = JN
#         self.name = name
#         self.runs = runs
#         self.wickets = wickets
#         self.team_name = team_name

# p1 = PlayerInfo(45, "Rohit Sharma", 520, 0, "Mumbai Indians")
# p2 = PlayerInfo(77, "Suryakumar Yadav", 480, 0, "Mumbai Indians")
# p3 = PlayerInfo(63, "Ishan Kishan", 430, 0, "Mumbai Indians")
# p4 = PlayerInfo(33, "Tilak Varma", 370, 0, "Mumbai Indians")
# p5 = PlayerInfo(99, "Hardik Pandya", 310, 10, "Mumbai Indians")
# p6 = PlayerInfo(93, "Tim David", 250, 0, "Mumbai Indians")
# p7 = PlayerInfo(8, "Piyush Chawla", 20, 18, "Mumbai Indians")
# p8 = PlayerInfo(94, "Gerald Coetzee", 15, 20, "Mumbai Indians")

# team_MI =[]
# team_MI.append(p1)
# print(team_MI)

class Student:
    def __init__(self,r,n,m):
        self.__name = n
        self.__roll = r
        self.__marks = m
    
    def getName(self):
        return self.name  
    def setName(self, newName):
        self.name = newName
    def getName(self):
        return self.__roll  
    def setName(self, newRoll):
        self.roll = newRoll
    def getName(self):
        return self.__marks  
    def setName(self, newMarks):
        self.marks = newMarks
    
    def display(self):
        print(f"roll number : {self.__roll} \nname is : {self.__name}\nmarks of {self.__name} is {self.__marks}")
    

