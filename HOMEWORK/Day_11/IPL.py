import Player_Info as p

def set_team():
    tname = input("Enter team name :")
    if tname == 'CSK' or tname == 'csk':
        tname = p.CSK_Team
    elif tname == 'RCB' or tname == 'rcb':
        tname = p.RCB_Team
    elif tname == 'MI' or tname == 'mi':
        tname = p.MI_Team
    else:
        print("Enterd Team name is invalid Try Again !!!")
    return tname

def main_file():
    team = ""
    ch = 0
    while ch != 6: 
        print('$'*50,"IPL TEAM STATISTICS",'$'*50)
        print("1. SHOW CAPTAIN OF THE TEAM")
        print("2. SHOW ALL TEAM PLAYER INFORMATION")
        print("3. SHOW BEST BOLLER IN TEAM")    
        print("4. SHOW BEST BATTER IN TEAM")
        print("5. SHOW SPECIFIC PLAYER INFORMATION")
        print("6. EXIT")
        ch = int(input("Enter Your Choice :"))
        if ch == 1:
            
            team = set_team()
            # logic for find captain from team list 
            captain = list(filter(lambda x:x.getCap() !='' ,team))
            for p in captain:
                print(f"Captain of {p.getTeamName()} is {p.getPName()}")
        
        elif ch == 2:
            team = set_team()
            tn = team[0]
            print(f"\t\t","#"*15,"All Player in ",tn.getTeamName()," are ","*"*15,"\n")
            for p in team:
                print(f"\t{p.getCap()}\tJersy No: {p.getJName()}  \t Name : {p.getPName()}\t\t",f" Runs: {p.getRuns()}\t wicket : {p.getWicket()}   ")     
    
        elif ch == 3:
            team = set_team()
            Best_Boller = list(filter(lambda x:x.getWicket()>10,team))
            
            tn = team[0]
            print(f"#"*15,"Best Boller in ",tn.getTeamName(),"*"*15,"\n\n")
            
            for p in Best_Boller:
                print(f"Jersy No:{p.getJName()}  {p.getPName()} took {p.getWicket()} wickets\n")
            
        elif ch == 4:
            team = set_team()
            Best_Boller = list(filter(lambda x:x.getRuns()>350,team))
            
            tn = team[0]
            print(f"#"*15,"Best Batsman in ",tn.getTeamName(),"*"*15,"\n\n")
            
            for p in Best_Boller:
                print(f"Jersy No:{p.getJName()}  {p.getPName()} Make {p.getRuns()} Runs\n")
        
        elif ch == 5:
            team = set_team()
            player  = input("Enter player name or jersy no :")
            try:
                jn = int(player)
                P_Info = list(filter(lambda x: x.getJName() == jn ,team))
                for i in P_Info:
                    print(f"\t{i.getCap()}\tJersy No: {i.getJName()}  \t Name : {i.getPName()}\t\t",f" Runs: {i.getRuns()}\t wicket : {i.getWicket()}   ")  
            except:
                P_Info = list(filter(lambda x: x.getPName() == player ,team))
                for i in P_Info:
                    print(f"\t{i.getCap()}\tJersy No: {i.getJName()}  \t Name : {i.getPName()}\t\t",f" Runs: {i.getRuns()}\t wicket : {i.getWicket()}   ") 
                      
            
         
main_file()