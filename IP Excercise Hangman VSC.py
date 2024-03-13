secretword = "daylight"
guessed_letters = []
chances = 8

while chances > 0:
    guess = input("guess a letter in my secret word:")

    if len(guess) !=1:
        print("please give me one letter.")
    elif not guess.isalpha():
        print("please give me a letter.")
    elif guess.lower() in guessed_letters:
        print("you already guessed that letter.")
    else:
        guessed_letters.append(guess.lower())
        if guess.lower() in secretword.lower():
            print("congrats, you guessed a letter!")
        else:
            chances-=1
            print("better luck next time. you have {} chances left".format(chances))
        display = ""
        for letter in secretword:
            if letter.lower() in guessed_letters:
                display +=letter
            else:
                display +="_"
        print(display)

        if "_" not in display:
            print("conratulations! you guessed the word:", secretword)
            break

        if chances == 0:
            print("sorry, you ran out of chances. the word was:", secretword)