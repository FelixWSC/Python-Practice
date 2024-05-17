play = "yes"
while play == "yes":
    score = 0
    # Ask the user their name and save it
    name = input("What is your name?")
    # Greet the user and introduce the quiz
    print("Welcome to this quiz,", name )
    print("This quiz is about different animals.")
    
    while True:
        try:
            tries = input("How many attempts do you want at each question? 1- 3")
            tries = int(tries)
            break 
        except: 
            print("That's not a number")
            
    import random 
    GOOD_COMMENTS = ["Amazing!", "Lets go!", "Keep it up", "Nice work!"]
    BAD_COMMENTS = ["Dont give up", "Keep trying", "You got next one!"]
    
    # Question 1
    question_attempts = tries
    while question_attempts > 0:
            QUESTION_FORMAT = "{}\nA.{}B.{}C.{}D.{}"
            question = "What bird can fly the highest?"
            a= "Peregrine falcon"
            b= "Andean condor"
            c= "Rüppell'sVulture"
            d= "Whooper swan"
            # Question 1 answer
            answer = input (QUESTION_FORMAT.format(question, a, b, c, d)).lower()
            if answer == c or answer == "c" or answer == "Rüppell'sVulture" or answer == "Ruppells Vulture".lower():
                print("Correct!")
                score +=5
                print(random.choice (GOOD_COMMENTS))
                break
            elif  answer == (""):
                print("I see you didn't write anything")
                print(random.choice (BAD_COMMENTS))
            else :
                print("Incorrect")
                print(random.choice (BAD_COMMENTS))
        
            question_attempts -= 1
    print("The answer is the Rüppell's Vulture")


    # Question 2
    question_attempts = tries
    while question_attempts > 0:
            QUESTION_FORMAT = "{}\nA.{}B.{}C.{}D.{}"
            question = "What is the fastest water animal?"
            a= "Sailfish"
            b= "Shark"
            c= "Marlin"
            d= "Orca"
            # Question 2 answer
            answer = input (QUESTION_FORMAT.format(question, a, b, c, d)).lower()
            if answer == a or answer == "a" or answer == "Sailfish".lower():
                print("Correct!")
                score +=5
                print(random.choice (GOOD_COMMENTS))
                break
            elif  answer == (""):
                print("I see you didn't write anything")
                print(random.choice (BAD_COMMENTS))
            else :
                print("Incorrect")
                print(random.choice (BAD_COMMENTS))
        
            question_attempts -= 1
    print("The fastest water animal is the sailfish.")

    # Question 3
    
    question_attempts = tries
    while question_attempts > 0:
            QUESTION_FORMAT = "{}\nA.{}B.{}C.{}D.{}"
            question = "How many birds species are there in the world?"
            a= "2,000"
            b= "11,000"
            c= "100,000"
            d= "23,000"
            # Question 2 answer
            answer = input (QUESTION_FORMAT.format(question, a, b, c, d)).lower()
            if answer == b or answer == "b" or answer == "11,000" or answer == "11000":
                print("Correct!")
                score +=5
                print(random.choice (GOOD_COMMENTS))
                break
            elif  answer == (""):
                print("I see you didn't write anything")
                print(random.choice (BAD_COMMENTS))
            else :
                print("Incorrect")
                print(random.choice (BAD_COMMENTS))
        
            question_attempts -= 1
    print("There are more than 11,000 unique bird species in the world.")

    # Question 4
    question_attempts = tries
    while question_attempts > 0:
            QUESTION_FORMAT = "{}\nA.{}B.{}C.{}D.{}"
            question = "what mammal has no vocal cords?"
            a= "Sloth"
            b= "Skunk"
            c= "Giraffe "
            d= "Cheetah"
            # Question 2 answer
            answer = input (QUESTION_FORMAT.format(question, a, b, c, d)).lower()
            if answer == a or answer == "a" or answer == "Sloth".lower() or answer == "The Sloth".lower():
                print("Correct!")
                score +=5
                print(random.choice (GOOD_COMMENTS))
                break
            elif  answer == (""):
                print("I see you didn't write anything")
                print(random.choice (BAD_COMMENTS))
            else :
                print("Incorrect")
                print(random.choice (BAD_COMMENTS))
        
            question_attempts -= 1
    print("The Sloth dosen't have any vocal chords.")

    # Question 5
    question_attempts = tries
    while question_attempts > 0:
            QUESTION_FORMAT = "{}\nA.{}B.{}C.{}D.{}E.{}"
            question = "How many years can a snail sleep for?"
            a= "1 year"
            b= "100 years"
            c= "4 years"
            d= "3 years"
            e= "0 years"
            # Question 5 answer
            answer = input (QUESTION_FORMAT.format(question, a, b, c, d,e)).lower()
            if answer == d or answer == "d" or answer == "3" or answer == "3 Years".lower():
                print("Correct!")
                score +=5
                print(random.choice (GOOD_COMMENTS))
                break
            elif  answer == (""):
                print("I see you didn't write anything")
                print(random.choice (BAD_COMMENTS))
            else :
                print("Incorrect")
                print(random.choice (BAD_COMMENTS))
                question_attempts -= 1
    print("Snails can actually sleep up to three years.")


    # End the quiz
    print("Thank you for trying my quiz {}, you got {} points!".format(name,score))
    play = input("Do you want to play again?")
print("Thank you for playing my quiz!")