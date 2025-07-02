# Movie Database Dictionary Program

## Overview
This Python program allows users to interact with a database of movies and their cast members from **2021 to 2025**. It provides options to **list all movies**, **filter movies by year**, **search for a particular movie's cast**, and **lookup actors across all movies**.

## Features
The program offers the following choices:
1. **Display all movies and their cast** - Lists all movies along with their respective cast members.
2. **Display movies, cast for a particular year** - Shows movies released in a specific year along with their cast.
3. **Search for a movie within a specific year** - Fetches the cast of a given movie for the selected year.
4. **Search for an actor/actress** - Finds all movies in which a particular actor/actress appeared.

## Usage
Upon running the program, users are prompted to select an option from the menu. Enter the corresponding number to proceed.

### Example Outputs:

### **1. Display All Movies and Their Cast**
      --------------Movie Database: --------
      ---------------Year: 2021----------------
       Sooryavanshi : ['Akshay Kumar', 'Katrina Kaif', 'Ajay Devgn'] 
       83 : ['Ranveer Singh', 'Deepika Padukone', 'Pankaj Tripathi'] 
       Antim: The Final Truth : ['Salman Khan', 'Aayush Sharma', 'Mahima Makwana'] ...
      --------------Year: 2025---------------- 
       Housefull 5 : ['Akshay Kumar', 'Riteish Deshmukh', 'John Abraham'] ...

### **2. Display movies, cast for a particular year**
     Enter year :2021

    ---------------Year: 2021 ----------------
    ------ In year  2021  released movie list are --------

    Sooryavanshi : ['Akshay Kumar', 'Katrina Kaif', 'Ajay Devgn']
    83 : ['Ranveer Singh', 'Deepika Padukone', 'Pankaj Tripathi']
    Antim: The Final Truth : ['Salman Khan', 'Aayush Sharma', 'Mahima Makwana']
    Bell Bottom : ['Akshay Kumar', 'Vaani Kapoor', 'Huma Qureshi']
    Chandigarh Kare Aashiqui : ['Ayushmann Khurrana', 'Vaani Kapoor']
    Tadap : ['Ahan Shetty', 'Tara Sutaria']

### **3. Search for a movie within a specific year** 
     Enter year :2024

    ---------------Year: 2024 ----------------

    ------ In year  2024  released movie list are --------

          Stree 2
          Bhool Bhulaiyaa 3
          Singham Again
          Fighter
          Shaitaan
          Crew
          # ask for enter movie name to display that movie details
    Enter movie name :Crew
    Crew : ['Tabu', 'Kareena Kapoor', 'Kriti Sanon']
    Total cast work in this movie : 3

###  **4. Search for an actor/actress**
    Total cast in all movies :
    {'Ranveer Singh', 'Nagarjuna Akkineni', 'Tara Sutaria', 'Darshan Kumaar', 'Anil Kapoor', 'Manushi Chhillar', 'Indraneil Sengupta', 'Jyotika', 'Ranbir Kapoor', 'Shraddha Kapoor', 'Akshaye Khanna', 'Utkarsh Sharma', 'Ameesha Patel', 'Kiara Advani', 'Pankaj Tripathi', 'Hrithik Roshan', 'Darsheel Safary', 'Salman Khan', 'Vaani Kapoor', 'Nayanthara', 'Ronit Roy', 'Shantanu Maheshwari', 'Ajay Devgn', 'Vijay Raaz', 'Ahan Shetty', 'Ayushmann Khurrana', 'Sunny Deol', 'Nushrratt Bharuccha', 'Aayush Sharma', 'Akshay Kumar', 'Deepika Padukone', 'Mithun Chakraborty', 'Shah Rukh Khan', 'Huma Qureshi', 'Riteish Deshmukh', 'John Abraham', 'Jacqueline Fernandez', 'Kareena Kapoor', "Genelia D'Souza", 'Anupam Kher', 'Mahima Makwana', 'Vijay Sethupathi', 'Emraan Hashmi', 'Rajkummar Rao', 'Rashmika Mandanna', 'Aamir Khan', 'Taapsee Pannu', 'R. Madhavan', 'Kajol', 'Kriti Sanon', 'Dhanush', 'Parineeti Chopra', 'Boman Irani', 'Medha Shankr', 'Saurabh Shukla', "Ileana D'Cruz", 'Amitabh Bachchan', 'Katrina Kaif', 'Tabu', 'Alia Bhatt', 'Kartik Aaryan'}

    Enter actor name :Alia Bhatt
    
    year : 2022 : , Movie Name : Brahmāstra: Part One – Shiva : ['Ranbir Kapoor', 'Alia Bhatt', 'Amitabh Bachchan']
    year : 2022 : , Movie Name : Gangubai Kathiawadi : ['Alia Bhatt', 'Shantanu Maheshwari', 'Vijay Raaz']
    
    Alia Bhatt Casted in  2  movies