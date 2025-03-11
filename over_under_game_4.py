


import random

class game:
    def __init__(self):
        largest = 100
        early_end = 5
        score = 0
        guesses = 0
        all_guesses = []
        answer = random.randrange(1, largest)

    def select(self):
        option = input("Would you like to play the hard or calm version?: ")
        if option == 'hard':
            self.over_under_4_2()
        elif option == 'calm':
            self.over_under_4()
        else:
            print("Not an answer.")
            self.select()

    #Calm Version
    def over_under_4(self):
        game_running = True
        while game_running:
            #print(answer)
            guess = int(input(f"Over or Under, 1 - {str(largest)}: "))
            self.all_guesses.append(guess)
            if guess == -222:
                print("You may now see the answer for testing.")
                print(answer)
                del all_guesses[-1]
            elif guess == 0:
                if early_end == 5:
                    del all_guesses[-1]
                    print("0 is under the range of 1 - 100. Please guess again.")
                else:
                    del all_guesses[-1]
                    large = max(all_guesses)
                    small = min(all_guesses)
                    print("Thanks For Playing! Final Score =", score)
                    print("All Guesses =", all_guesses, "Largest guess is =", large, "Smallest guess is =", small)
                    game_running = False
                    return
            elif guess < answer:
                guesses = guesses + 1
                print("Over")
            elif guess > answer:
                guesses = guesses + 1
                print("Under")
            elif guess == answer:
                large = max(all_guesses)
                small = min(all_guesses)
                score = score + 1
                guesses = guesses + 1
                largest = largest + 100
                early_end = 6
                print("You got the answer! Keep playing as the range increases by 100! Press 0 to stop!")
                print("Guesses this round =", guesses)
                print("All Guesses so far =", all_guesses, "Largest guess =", large, "Smallest guess =", small)
                print("Score =", score)
                guesses = guesses - guesses
                answer = random.randrange(1, largest)
                self.over_under_4()
            else:
                print("How did you get here?")

    #Hard version
    def over_under_4_2(self):
        game_running = True
        while game_running:
            #print(answer)
            guess = input(f"Over or Under, 1 - {str(largest)}, 10 guesses per turn: \n")
            try:
                guess = int(guess)
            except:
                print("Must be a number")
            else:
                all_guesses.append(guess)
                if guess == answer:
                    score = score + 1
                    guesses = guesses + 1
                    largest = largest + 100
                    early_end = 6
                    large = max(all_guesses)
                    small = min(all_guesses)
                    print("You got the answer! Keep playing as the range increases by 100! Press 0 to stop!")
                    print("Guesses this round =", guesses)
                    print("All Guesses so far =", all_guesses, "Largest guess =", large, "Smallest guess =", small)
                    print("Score =", score)
                    guesses = guesses - guesses
                    answer = random.randrange(1, largest)
                    over_under_4_2()
                elif guesses > 8:
                    print("You lost")
                    large = max(all_guesses)
                    small = min(all_guesses)
                    print("Thanks For Playing! Final Score =", score)
                    print("All Guesses =", all_guesses, "Largest guess is =", large, "Smallest guess is =", small)
                    game_running = 2
                elif guess == -222:
                    print("You may now see the answer for testing use.")
                    print(answer)
                    del all_guesses[-1]
                elif guess == 0:
                    if early_end == 5:
                        del all_guesses[-1]
                        print("0 is under the range of 1 - 100. Please guess again.")
                    else:
                        del all_guesses[-1]
                        large = max(all_guesses)
                        small = min(all_guesses)
                        print("Thanks For Playing! Final Score =", score)
                        print("All Guesses =", all_guesses, "Largest guess is =", large, "Smallest guess is =", small)
                        game_running = False
                        return
                elif guess < answer:
                    guesses = guesses + 1
                    print("Over")
                    print("You have", 10 - guesses, "guesses left.")
                elif guess > answer:
                    guesses = guesses + 1
                    print("Under")
                    print("You have", 10 - guesses, "guesses left.")
                else:
                    print("How did you get here?")




