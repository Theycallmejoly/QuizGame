def game ():

    print("Welcome to the Game! I hope that you enjoy")

    DesireToPlay = input("Are you Ready? ")

    if DesireToPlay:
        print("Here we Go !!!!!")
        print("Dont forget that each 3 mistakes will remove one of your scores!!!")
    else:
        print("Hope that you change your mind next time. Bye Bye !!:(")
        quit()

    score = 0
    mistakes = 0

    userAnswer = input("What is the capital of France?").lower()
    if userAnswer == "paris":
        print("Correct!")
        score += 1
    else:
        print ("Incorrect!")
        mistakes += 1
    
    userAnswer = input ("Who wrote the play Romeo and Juliet?").lower()
    if userAnswer == "william shakespeare":
        print("Correct!")
        score += 1
    else:
        print ("Incorrect!")
        mistakes += 1
    userAnswer = input("What is the chemical symbol for water?").lower()
    if userAnswer == "h2o":
        print("Correct!")
        score += 1
    else:
        print ("Incorrect!")
        mistakes += 1
    userAnswer = input("What is the tallest mammal in the world?").lower()
    if userAnswer == "Giraffe":
        print("Correct!")
        score += 1
    else:   
        print ("Incorrect!")
        mistakes += 1
    userAnswer = input("What is the powerhouse of the cell").lower()
    if userAnswer == "mitochondria":
        print("Correct!")
        score += 1
    else:   
        print ("Incorrect!")
        mistakes += 1
    userAnswer = input("In which year did World War II end?").lower()
    if userAnswer == "1945":
        print("Correct!")
        score += 1
    else:   
        print ("Incorrect!")
        mistakes += 1
    userAnswer = input("Who painted the Mona Lisa?").lower()
    if userAnswer == "leonardo da Vinci":
        print("Correct!")
        score += 1
    else:   
        print ("Incorrect!")
        mistakes += 1
    userAnswer = input("What is the largest planet in our solar system?").lower()
    if userAnswer == "jupiter":
        print("Correct!")
        score += 1
    else:   
        print ("Incorrect!")
        mistakes += 1

    userAnswer = input("Who developed the theory of relativity?").lower()
    if userAnswer == "albert einstein":
        print("Correct!")
        score += 1
    else:   
        print ("Incorrect!")
        mistakes += 1

    userAnswer = input("What is the primary ingredient in guacamole?").lower()
    if userAnswer == "avocado":
        print("Correct!")
        score += 1
    else:   
        print ("Incorrect!")
        mistakes += 1

    if mistakes >= 3:
        deduction = mistakes // 3  
        score -= deduction
        print(f"Since you made {mistakes} mistakes, {deduction} point{'s' if deduction > 1 else ''} {'are' if deduction > 1 else 'is'} deducted from your score.")
        print("Your revised score is:", score)



    print("Your final score is:", score)

game()

userResponse = input("Would you like to play again?").lower()

while userResponse == "yes" :
    game()
    break
print("See you soon!!")
