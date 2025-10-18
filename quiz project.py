questions =[
    # question 1(1000)
    ["what is the capital of australia?","sydney","melbourne","canberra","perth", "none", 3],
    #question2(2000)
    ["which planet is known as red planet?","jupiter", "mars", "saturn", "venus"," none", 2],
    #question3(3000)
    ["who painted the mona lisa?","van gogh", "picasso", "da vinci", "monet", "none", 3],
    #question4(5000)
    ["what is the chemical symbol for gold?", "au", "pb", "fe", "cu", "none", 1],
    #question5(10,000)
    ["which ocean is the largest on the earth?", "atlantic", "indian", "pacific", "arctic", "none", 3],
    #question6(20,000)
    ["the famous silicon valley is located in which u.s state?", "new york", "texas", "california", "florida", "none", 3],
    #question7(40,000)
    ["how many sides does a heptagon have?", "six", "seven", "eight", "nine", "none", 2],
    #question8(80,000)
    ["in which year does the titanic sink?", "1912", "1905", "1923", "1931", "none", 1],
    # question9(1,60,000)
    ["which element has the atomic number1?", "oxygen", "helium", "hydrogen", "carbon", "none", 3],
    # question10(3,20,000)
    ["what is the smallest continent by land area?", "europe", "antarctica", "australia", "south america", "none", 3],
    # question11(6,40,000)
    ["who is credited by inventing printing press?","galileo", "gutenberg","edison", "tesla","none",2],
    # question12(12,50,000)
    ["which of these is not a programming language?", "python", "html", "c++","java","none",2],
    # question13
    ["the statue of liberty is gift for US from which country?", "spain","germay","france","italy","none",3],
    # question14(50,00,000)
    ["what is the proess in which plnts make their food?","respiration","photosynthesis","transpiration","none", 2],
    #question15(1,00,00,000)
    ["which ancient wonder was located in modern day-iraq?","hanging gardens of babyon", "pyramid of giza","statue of zeus","colossus of rhodes","none",1],
]


levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0

for i in range(len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}: {question[0]}")
    print(f"a. {question[1]}        b. {question[2]}")
    print(f"c. {question[3]}        d. {question[4]}")

    reply = int(input("Enter your answer (1-4): "))
    if reply == question[-1]:
        print(f"Correct answer! You have won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print(f"Incorrect answer. The correct answer was option {question[-1]}.")
        break
    if(i == 14):
        print("!!!CONGRATULATIONS!!!")
print(f"your take home money is {levels[i]}")
















































































# for i in range(0, len(questions)):
#     if i>=len(levels):
#         break
#     question = questions[i]

#     # level_amount = "{:,.of}".format(levels[i]).replace(",","X").replace(".",",").replace("X",",")
#     # level_amount = "{:,.2f}".format(levels[i]).replace(",", "X").replace(".", ",").replace("X", ",")

#     print(f"question for Rs. {levels[i]}")
#     print(f"a. {question[1]:<15}        b. {question[2]:<15}")
#     print(f"c. {question[3]:<15}        c. {question[4]:<15}")

#     reply = int(input("enter youranswer(0-4) or 0 to quit: \n"))
#     if (reply == 0):
#         if(i == 0):
#             money = 0
#         elif i <= 4:
#             money = 0
#         elif i <= 9:
#             money = 10000
#         else:
#             money = 320000
#         break
#     if (reply == question[-1]):
#         # print(f"correct answer!, you won Rs. {level_amount}")
#         if (i == 4):
#             money = 10000
#         elif(i == 9):
#             money = 320000
#         elif(i == 14):
#             money = 10000000
#         else:
#             money = levels[i]

#     else:
#         print("wrong answer!!")
#         if i < 5:
#             money = 0
#         elif i <10:
#             money = 10000
#         else:
#             money = 320000
#         break
# final_amount = "{:,2f}".format(money).replace(",","X").replace(".",",").replace("X",",")

# print(f"\n your take home money is Rs. {final_amount}")


