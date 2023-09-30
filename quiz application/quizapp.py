questions=("Which is the biggest continent in the world?",
            "Which is the longest river in the world?",
            "Which is the largest ocean in the world?",
            "Which is India’s first super computer?",
            "Which bank is called bankers Bank of India?")
options=(("A.North America","B.Asia","C.Africa","D.Australia"),
("A.Great Ganga","B.Nile","C.Amazon","D.Niger"),
("A.Indian Ocean","B.Pacific Ocean","C.Arctic Ocean","D.Atlantic Ocean"),
("A.Param8000","B.param80000","C.param800","D.param8"),
("A.Reserve Bank of India","B.Punjab National Bank","C.State Bank of India","D.ICICI Bank"))
answers=("B","B","B","A","A")
guesses=[]
question_num=0
score=0
for question in questions:
    print("------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("enter(A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f'{answers[question_num]} is the correct answer')
    question_num += 1
print("RESULTS:::")
print("answers:",end="")
for answer in answers:
    print(answer,end=" ")
print()
print("guesses: ",end="")
for guess in guesses:
    print(guess,end=" ")
print()
score=(score / len(questions) * 100)
print(f"score:{score}%")