# make multiple dictionary by name movie_db_[year] from 2021 to 2025 total 4 dictionary
movie_db_2021 ={
    "Sooryavanshi": ["Akshay Kumar", "Katrina Kaif", "Ajay Devgn"],
    "83": ["Ranveer Singh", "Deepika Padukone", "Pankaj Tripathi"],
    "Antim: The Final Truth": ["Salman Khan", "Aayush Sharma", "Mahima Makwana"],
    "Bell Bottom": ["Akshay Kumar", "Vaani Kapoor", "Huma Qureshi"],
    "Chandigarh Kare Aashiqui": ["Ayushmann Khurrana", "Vaani Kapoor"],
    "Tadap": ["Ahan Shetty", "Tara Sutaria"]
}

movie_db_2022 = {
    "Brahmāstra: Part One – Shiva": ["Ranbir Kapoor", "Alia Bhatt", "Amitabh Bachchan"],
    "Drishyam 2": ["Ajay Devgn", "Tabu", "Akshaye Khanna"],
    "The Kashmir Files": ["Anupam Kher", "Mithun Chakraborty", "Darshan Kumaar"],
    "Bhool Bhulaiyaa 2": ["Kartik Aaryan", "Kiara Advani", "Tabu"],
    "Gangubai Kathiawadi": ["Alia Bhatt", "Shantanu Maheshwari", "Vijay Raaz"],
    "Ram Setu": ["Akshay Kumar", "Jacqueline Fernandez", "Nushrratt Bharuccha"]
}

movie_db_2023 = {
    "Jawan": ["Shah Rukh Khan", "Nayanthara", "Vijay Sethupathi"],
    "Pathaan": ["Shah Rukh Khan", "Deepika Padukone", "John Abraham"],
    "Animal": ["Ranbir Kapoor", "Parineeti Chopra", "Anil Kapoor"],
    "Gadar 2": ["Sunny Deol", "Ameesha Patel", "Utkarsh Sharma"],
    "Dunki": ["Shah Rukh Khan", "Taapsee Pannu", "Boman Irani"],
    "Tiger 3": ["Salman Khan", "Katrina Kaif", "Emraan Hashmi"]
}

movie_db_2024 = {
    "Stree 2": ["Rajkummar Rao", "Shraddha Kapoor", "Pankaj Tripathi"],
    "Bhool Bhulaiyaa 3": ["Kartik Aaryan", "Kiara Advani", "Tabu"],
    "Singham Again": ["Ajay Devgn", "Deepika Padukone", "Ranveer Singh"],
    "Fighter": ["Hrithik Roshan", "Deepika Padukone", "Anil Kapoor"],
    "Shaitaan": ["Ajay Devgn", "R. Madhavan", "Jyotika"],
    "Crew": ["Tabu", "Kareena Kapoor", "Kriti Sanon"]
}

movie_db_2025 = {
    "Housefull 5": ["Akshay Kumar", "Riteish Deshmukh", "John Abraham"],
    "Sitaare Zameen Par": ["Aamir Khan", "Genelia D'Souza", "Darsheel Safary"],
    "Maalik": ["Rajkummar Rao", "Manushi Chhillar", "Medha Shankr"],
    "Kuberaa": ["Dhanush", "Rashmika Mandanna", "Nagarjuna Akkineni"],
    "Maa": ["Kajol", "Ronit Roy", "Indraneil Sengupta"],
    "Raid 2": ["Ajay Devgn", "Ileana D'Cruz", "Saurabh Shukla"]

}
big_movie_db = {
    2021: movie_db_2021,
    2022: movie_db_2022,
    2023: movie_db_2023,
    2024: movie_db_2024,
    2025: movie_db_2025
}

# to display all movie name and their cast from big database
print("Movie Database:")
print("1.To Display all movie name and their cast :->")
print("2.To Display all movie name and their cast in a particular year :->")
print("3.To Display all movie name and their cast in a particular year and particular movie :->")
print("4. Search movie actor/actress name :->")
ch = int(input("Enter your choice :"))

while(ch!=0):
    if ch==1:
        for year in big_movie_db.keys():
            print()
            print("---------------Year:",year,"----------------")
            print()
            for movie,cast in big_movie_db[year].items():
                print(movie,":",cast)
        ch = int(input("Enter your choice :"))
    elif ch==2:
        year = int(input("Enter year :"))
        if year in big_movie_db.keys():
            print()
            print("---------------Year:",year,"----------------")
            print()
            print("------ In year ", year, " released movie list are --------")
            print()
            for movie,cast in big_movie_db[year].items():
                print(movie,":",cast)
            ch = int(input("Enter your choice :"))
        else:
            print("Year not found")
    elif ch==3:
        year = int(input("Enter year :"))
        if year in big_movie_db.keys():
            print()
            print("---------------Year:",year,"----------------")
            print()
            print("------ In year ", year, " released movie list are --------")
            print()
            for movie,cast in big_movie_db[year].items():
                 print("         ",movie)
            movie = input("Enter movie name :")
            if movie in big_movie_db[year].keys():
                print(movie,":",big_movie_db[year][movie])
                print("Total cast work in this movie :",len(cast))
            else:
                print("Movie not found")
        else:
            print("Year not found")
        ch = int(input("Enter your choice :"))
    elif ch==4:
        count=0
        L2 = []
        for year in big_movie_db.keys():
            for movie,cast in big_movie_db[year].items():
               for actor in cast:
                   L2.append(actor)
     
        print("Total cast in all movies :")
        L2= set(L2)
        print(L2)
        actor = input("Enter actor name :")
        for year in big_movie_db.keys():
            for movie,cast in big_movie_db[year].items():
                if actor in cast:
                    print("year :",year,": , Movie Name :",movie,":",cast)
                    count+=1
        print(actor,"Casted in ", count," movies")
        ch = int(input("Enter your choice :"))

    else:
        print("Invalid choice")
        ch = int(input("Enter your choice :"))