#This is the quiz fortune challenge
#This challenge consists of of 50 questions and the cash price of Rs-1,00,000/-


    #list the questions
questions = [

    "1.What is the capital of India?",
    "2.What is the national currency of Japan?",
    "3.What is the latest version of Python released in 2025?",
    "4.What is the chemical symbol of Gold?",
    "5.What is the largest planet in our Solar System?",
    "6.What is the full form of AI?",
    "7.What is the technology behind ChatGPT?",
    "8.What is the official programming language of Android app development?",
    "9.What is the national animal of India?",
    "11.What is the square root of 144?",
    "12.What is the chemical formula of Water?",
    "13.What is the fastest land animal?",
    "14.What is the national game of India?",
    "15.What is the longest river in the world?",
    "16.What is the largest ocean on Earth?",
    "17.What is the name of the first Indian satellite?",
    "18.What is the full form of NASA?",
    "19.What is the smallest prime number?",
    "20.What is the process of plants making food called?",
    "21.What is the full form of HTTP?",
    "22.What is the main gas in Earth’s atmosphere?",
    "23.What is the binary value of decimal 10?",
    "24.What is the currency of the United Kingdom?",
    "25.What is the speed of light in vacuum (approx)?",
    "26.What is the SI unit of Force?",
    "27.What is the shape of Earth?",
    "28.what is  study of rocks called?"  ,       
    "29.What is the main source of energy for Earth?",
    "30.What is the national flower of India?",
    "31.What is the latest iPhone model launched in 2025?",
    "32.What is the headquarters of Google located?",
    "33.What is the chemical symbol of Sodium?",
    "34.What is the programming language used in Data Science?",
    "35.What is the main function of the CPU?",
    "37.What is the capital of Australia?",
    "38.What is the national bird of India?",
    "39.What is the largest desert in the world?",
    "40.What is the freezing point of water in Celsius?",
    "41.What is the hottest planet in our Solar System?",
    "42.What is the basic unit of Life?",
    "43.What is the national currency of China?",
    "44.What is the study of earthquakes called?",
    "45.What is the boiling point of water in Celsius?",
    "46.What is the capital of France?",
    "47.What is the national anthem of India?",
    "48.What is the opposite of Artificial?",
    "49.What is the capital of Canada?",
    "50.What is the name of the galaxy we live in?",
    ]

    #the answers of the questions
    
answers = [
    "Delhi",
    "Yen",
    "Python 3.14",
    "Au",
    "Jupiter",
    "Artificial Intelligence",
    "Artificial Intelligence",
    "Java",
    "Tiger",
    "12",
    "H2O",
    "Cheetah",
    "Hockey",
    "Nile",
    "Pacific Ocean",
    "Aryabhata",
    "National Aeronautics and Space Administration",
    "2",
    "Photosynthesis",
    "Hyper Text Transfer Protocol",
    "Nitrogen",
    "1010",
    "Pound Sterling",
    "3*10^8 m/s",
    "Newton",
    "Spherical",
    "Geology",
    "Sun",
    "Lotus",
    "iPhone 16",
    "California",
    "Na",
    "Python",
    "Processing Data",
    "Canberra",
    "Peacock",
    "Sahara",
    "0",
    "Venus",
    "Cell",
    "Yuan",
    "Seismology",
    "100",
    "Paris",
    "Jana Gana Mana",
    "Natural",
    "Ottawa",
    "Milky Way",
    "Sumo Wrestling",
    "Diamond",
]


# setting the rewards

total_cash_price = 100000
total_questions = 50
cash_per_question = total_cash_price // total_questions

#initialize the quiz's variables

score = 0
cash_won = 0

# welcoming the user 
print("\n ## welcome to the quiz fortune challenge ##")
print("Answer all questions  correctly to win 100000/- ")

#quiz execution
#using for loop

for i in range(total_questions):
    print(f"{questions[i]}")
    user_answer = input("your answer: ").strip()

    if user_answer.lower() == answers[i].lower():
        print("##correct##\n")
        score += 1
        cash_won += cash_per_question
    else:
        print(f"!!Wrong!! correct answer: {answers[i]}\n")

print("##QUIZ COMPLETED##")
print(f"your_score: {score}/{total_questions}")
print(f"cash_price_won: Rs.{cash_won}/-")