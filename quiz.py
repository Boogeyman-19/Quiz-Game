questions=("What is the name of the largest ocean in the world ? ",
           "What is the name of the tallest mountain peak in the world ?",
           "What is the name of the biggest planet in the solar system ?",
           "What is the name of the longest river in the world ?",
           "What is the name of the most popular sport in the world ?")
options=(("A.Indian Ocean","B.Pacific Ocean","C.Atlantic Ocean","D.Arctic Ocean"),
         ("A.Mount Everest","B.Mount Kilimanjaro","C.K2","D.Kangchenjunga"),
         ("A.Jupiter","B.Earth","C.Venus","D.Satrun"),
         ("A.Godavari River","B.Yangtze River","C.Amazon River","D.Nile River"),
         ("A.Football","B.Cricket","C.BaseBall","D.BasketBall"))
answers=("B","A","A","D","A")
guesses=[]
score=0
question_idx=0
print("\n\n********WELCOME TO THE QUIZ GAME********")
for question in questions:
    print("---------------------------------------------------------------------")
    print(question)
    for option in options[question_idx]:
        print(option)
    guess=input("\nenter your option :").upper()
    guesses.append(guess)
    if guess==answers[question_idx]:
        score+=1
        print("\nYour Answer Is Correct!\n")
    else:
        print("\nYour Answer Is InCorrect!\n")
        print(f"{answers[question_idx]} is the correct answer...")
    question_idx+=1
print("---------------------------------------------------------------------")
print("\t\t\tSCORE BOARD\t\t\t")
print("---------------------------------------------------------------------")
print()
print(f"Your Final Score is:{score}")
print()
print()
