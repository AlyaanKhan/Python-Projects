import random
def guess_number():
    while(True):
        number = random.randint(0, 100)
        num_guess = int(input("Enter number to be guessed:: "))
        if num_guess < number:
            print("Too Low number!")
            print("You loose, TryAgain")
            print("The answer was:", number)
            play_again = input("Do you want to play again (Y/N):").strip().upper()
            if play_again != 'Y':
                print("Thank you for playing game!")
                return
        elif num_guess > number:
            print("Too High number!")
            print("You loose, TryAgain")
            print("The answer was:", number)
            play_again = input("Do you want to play again (Y/N):").strip().upper()
            if play_again != 'Y':
                print("Thank you for playing game!")
                return
        else:
            print("You Win! ")
guess_number()
        
