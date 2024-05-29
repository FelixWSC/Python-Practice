QUESTION_FORMAT = "{}\nA.{}B.{}C.{}D.{}"
import random 
GOOD_COMMENTS = ["Amazing!", "Lets go!", "Keep it up", "Nice work!"]
BAD_COMMENTS = ["Dont give up", "Keep trying", "You got next one!"]
QUESTIONS = ["What bird can fly the highest?",
             "What is the fastest water animal?",
                "How many birds species are there in the world?",
                "what mammal has no vocal cords?",
                "How many years can a snail sleep for?" ]
OPTIONS = [["Peregrine falcon", "Andean condor", "Rüppell'sVulture", "Whooper swan"],
           ["Sailfish", "Shark", "Marlin", "Orca"],
           ["2,000", "11,000", "100,000", "23,000"],
           ["Sloth", "Skunk", "Giraffe ", "Cheetah"],
           ["1 year", "100 years", "4 years", "3 years","0 years"]]
SHORT_OPTIONS = ["a", "b", "c", "d", "e"]
ANSWERS = [2,0,1,0,3]
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
            
    
    

    # Loop through each question/answers
    for i in range(len(QUESTIONS)):
        question_attempts = tries
        while question_attempts > 0:
            answer = input (QUESTION_FORMAT.format(QUESTIONS[i],OPTIONS[i][0],
                                                    OPTIONS[i][1], OPTIONS[i][2], OPTIONS[i][3])).lower()
            
            # Check the user's
            if answer == OPTIONS[i][ANSWERS[i]] or answer == SHORT_OPTIONS[ANSWERS[i]]:
                print("Correct!")
                score +=5
                print(random.choice (GOOD_COMMENTS))
                break
            elif  answer in SHORT_OPTIONS or answer in OPTIONS[i]:
                print("Wrong")
                print(random.choice (BAD_COMMENTS))
                question_attempts -= 1
            else :
                print("I see you didn't write anything")
                question_attempts -= 1
        print("The answer was the "+ str(OPTIONS[i][ANSWERS[i]]))



    # End the quiz
    print("Thank you for trying my quiz {}, you got {} points!".format(name,score))
    play = input("Do you want to play again?")
print("Thank you for playing my quiz!")

#print("The answer is the Rüppell's Vulture")
#print("The fastest water animal is the sailfish.")
#print("There are more than 11,000 unique bird species in the world.")
#print("The Sloth dosen't have any vocal chords.")
#print("Snails can actually sleep up to three years.")