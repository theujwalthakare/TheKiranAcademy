# 

cast1 = ["Himesh", "Supriya","nat"]
cast2 = ["Shahrukh", "Kajol","varun"]
cast3 = ["Joaquin", "Zazie"]
cast4 = ["RDJ","hulk","natasha"]
name1 = "Raaz"
name2="Dilwale"
name3="housfull5" 
name4="avengers"

movie_db= {}
movie_db[name1] = cast1
movie_db[name2] = cast2
movie_db[name3] = cast3
movie_db[name4] = cast4
print(movie_db)
print(movie_db[name1])

# for key in movie_db[name1]:
#     print(key)

# for name in movie_db.keys():
#     print(name ,":", movie_db[name])

# print(movie_db.values())
# for data in movie_db.values():
#     for cast in data:
#         if cast == "nat":
#             print(cast)
#     print()

for k,v in movie_db.items():
    # print(t)
    # k,v = t       
    print(k,":",v)
    
#