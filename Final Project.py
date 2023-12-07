score = 0

def addScore():
    global score
    score += 1
    print("Your current score is", score)

def main():

    print("Hello! Do you think you know Taylor Swift? Today we are going to find out with a quiz game!")
    ready = input("Are you ready for it? (answer yes or no)")
    while ready == "yes":
        print("Ok, let the games begin!")
        break
    else:
        print("too bad, you are playing anyways!")

    print("Let's start with an easy one: what is Taylor's lucky number?")
    luckyNum = int(input("Is it 27, 13, or 9?"))
    if luckyNum == 13:
        print("You got it! Her favorite number is 13!!")
        addScore()
    else:
        print("Good try, but her favorite number is actually 13!")
        print("Your current score is", score)

    print("Alright, next question: how many original albums does she have?")
    albums = int(input("Is it 4, 13, or 10?"))
    if albums == 10:
        print("That's right!! She has 10 original albums called Taylor Swift, Fearless, Speak Now, Red, 1989, Reputation, Lover, folklore, evermore, and Midnights")
        addScore()
    else:
        print("Nope, she has 10 original albums!")
        print("Your current score is", score)

    print("Ok, only a few more questions. Do you know how many Grammy nominations Taylor has?")
    nominations = int(input("Is it 52, 12, or 90?"))
    if nominations == 52:
        print("Yup! She has 52 Grammy nominations!")
        addScore()
    else:
        print("Sorry but she currently has 52 Grammy nominations")
        print("Your current score is", score)

    print("This year, Taylor released a remix of her hit song, Karma. Who was featured on this remix?")
    feature = input("Was it Ariana Grande, Ice Spice, or Pitbull?")
    if feature == "Ice Spice":
        print("You got it!")
        addScore()
    else:
        print("Wrong, it was Ice Spice!")
        print("Your current score is", score)

    print("2 more questions!")
    animal = input("Is she more of a dog or cat person?")
    if animal == "cat":
        print("That's right! She currently has 3 cats named Meredith, Olivia, and Benjamin")
        addScore()
    else:
        print("Good try, but she likes cats more!")
        print("Your current score is", score)

    print("Ok last question. It's gonna be a tough one. In 2012, Taylor released 2 songs, 'safe and sound' and 'eyes open' for a movie soundtrack.")
    movie = input("What is the name of the movie she wrote these songs for?")
    if movie == "The Hunger Games":
        print("Yay!!! You got it!")
        addScore()
    else:
        print("Ah, so close. It was actually The Hunger Games (best movie ever tbh)")
        print("Your current score is", score)

    print("Congrats! You completed the ultimate Taylor Swift trivia game! Let's see how many points you ended up with:")
    print(score)
    if score == 6:
        print("You got all of the questions correct. You must be the ultimate swiftie!")
    elif score > 3 and score < 6:
        print("Good job! You seem to know a little bit about Taylor!")
    else:
        print("You might wanna brush up on your Taylor Swift trivia and play again another time...")

    print("Thanks for playing!")



main()

