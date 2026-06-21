import random
def play_hangman():
    words = ["python" , "coding" , "laptop" , "planet" , "guitar"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts_left = 6

    print("--- Welcome to Hangman! ---")

    while attempts_left >0:
        display_word =""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "

            else:
                display_word += "_ "


        print(f"\nWord : {display_word}")
        print(f"Attempts left : {attempts_left}")
        print(f"Guessed so far : {', '.join(guessed_letters)}")

        #check for win 
        if "_" not  in display_word:
            print("Congratulations! You won!")
            break

        # get player input 
        guess  = input("Guess a letter :").lower()

        #basic validation
        if len(guess) != 1 or not guess.isalpha():
            print("please enter a single valid letter .")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'.Try again.")
            continue
        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts_left -= 1
            print(f"sorry, '{guess}' is not in the word.")
    if attempts_left == 0:
        print(f"\nGame Over ! You're out of attempts. The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()                


    

