class PlayerInfo():
    def __init__(self,JN,name,runs,wickets,team_name,TEAM_cap = ''):
        self.JN = JN
        self.name = name
        self.runs = runs
        self.wickets = wickets
        self.team_name = team_name
        self.captain = TEAM_cap
    
    def getJName(self):
        return self.JN
    def setJName(self,jersy_number):
        self.JN = jersy_number
    def getPName(self):
        return self.name
    def setPName(self,player_name):
        self.name = player_name
    def getRuns(self):
        return self.runs
    def setRuns(self,players_runs):
        self.runs = players_runs
    def getWicket(self):
        return self.wickets
    def setWicket(self,total_wicket):
        self.wickets = total_wicket
    def getTeamName(self):
        return self.team_name
    def setTeamName(self,team_name):
        self.team_name = team_name
    def getCap(self):
        return self.captain
    def setCap(self,captain):
        self.captain = captain
    
    
MI_Team = []
p1 = PlayerInfo(45, "Rohit Sharma", 520, 0, "Mumbai Indians")
p2 = PlayerInfo(77, "Suryakumar Yadav", 480, 0, "Mumbai Indians")
p3 = PlayerInfo(63, "Ishan Kishan", 430, 0, "Mumbai Indians")
p4 = PlayerInfo(33, "Tilak Varma", 370, 0, "Mumbai Indians")
p5 = PlayerInfo(99, "Hardik Pandya", 310, 10, "Mumbai Indians",'CAPTAIN')
p6 = PlayerInfo(93, "Tim David", 250, 0, "Mumbai Indians")
p7 = PlayerInfo(8, "Piyush Chawla", 20, 18, "Mumbai Indians")
p8 = PlayerInfo(94, "Gerald Coetzee", 15, 20, "Mumbai Indians")
p9 = PlayerInfo(23, "Romario Shepherd", 50, 5, "Mumbai Indians")
p10 = PlayerInfo(97, "Jasprit Bumrah", 12, 21, "Mumbai Indians")
p11 = PlayerInfo(55, "Akash Madhwal", 10, 15, "Mumbai Indians")
MI_Team.append(p1)
MI_Team.append(p2)
MI_Team.append(p3)
MI_Team.append(p4)
MI_Team.append(p5)
MI_Team.append(p6)
MI_Team.append(p7)
MI_Team.append(p8)
MI_Team.append(p9)
MI_Team.append(p10)
MI_Team.append(p11)


RCB_Team = []
p1 = PlayerInfo(18, "Virat Kohli", 680, 0, "Royal Challengers Bangalore")
p2 = PlayerInfo(97, "Faf du Plessis", 520, 0, "Royal Challengers Bangalore")
p3 = PlayerInfo(7, "Glenn Maxwell", 410, 8, "Royal Challengers Bangalore")
p4 = PlayerInfo(5, "Rajat Patidar", 380, 0, "Royal Challengers Bangalore",'CAPTAIN')
p5 = PlayerInfo(77, "Dinesh Karthik", 250, 0, "Royal Challengers Bangalore")
p6 = PlayerInfo(66, "Mahipal Lomror", 220, 0, "Royal Challengers Bangalore")
p7 = PlayerInfo(19, "Cameron Green", 320, 5, "Royal Challengers Bangalore")
p8 = PlayerInfo(99, "Mohammed Siraj", 10, 19, "Royal Challengers Bangalore")
p9 = PlayerInfo(94, "Yash Dayal", 5, 15, "Royal Challengers Bangalore")
p10 = PlayerInfo(11, "Lockie Ferguson", 8, 17, "Royal Challengers Bangalore")
p11 = PlayerInfo(74, "Karn Sharma", 12, 10, "Royal Challengers Bangalore")
RCB_Team.append(p1)
RCB_Team.append(p2)
RCB_Team.append(p3)
RCB_Team.append(p4)
RCB_Team.append(p5)
RCB_Team.append(p6)
RCB_Team.append(p7)
RCB_Team.append(p8)
RCB_Team.append(p9)
RCB_Team.append(p10)
RCB_Team.append(p11)

CSK_Team = []

p1 = PlayerInfo(7, "MS Dhoni", 180, 0, "Chennai Super Kings",'CAPTAIN')
p2 = PlayerInfo(31, "Ruturaj Gaikwad", 540, 0, "Chennai Super Kings")
p3 = PlayerInfo(8, "Devon Conway", 480, 0, "Chennai Super Kings")
p4 = PlayerInfo(5, "Ajinkya Rahane", 400, 0, "Chennai Super Kings")
p5 = PlayerInfo(25, "Shivam Dube", 450, 4, "Chennai Super Kings")
p6 = PlayerInfo(96, "Ravindra Jadeja", 180, 14, "Chennai Super Kings")
p7 = PlayerInfo(9, "Moeen Ali", 220, 10, "Chennai Super Kings")
p8 = PlayerInfo(29, "Deepak Chahar", 15, 12, "Chennai Super Kings")
p9 = PlayerInfo(99, "Matheesha Pathirana", 5, 20, "Chennai Super Kings")
p10 = PlayerInfo(90, "Tushar Deshpande", 8, 16, "Chennai Super Kings")
p11 = PlayerInfo(66, "Maheesh Theekshana", 10, 13, "Chennai Super Kings")

CSK_Team.append(p1)
CSK_Team.append(p2)
CSK_Team.append(p3)
CSK_Team.append(p4)
CSK_Team.append(p5)
CSK_Team.append(p6)
CSK_Team.append(p7)
CSK_Team.append(p8)
CSK_Team.append(p9)
CSK_Team.append(p10)
CSK_Team.append(p11)


