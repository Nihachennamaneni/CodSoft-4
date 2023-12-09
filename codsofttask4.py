import random

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and comp_choice == 'scissors') or (user_choice == 'scissors' and comp_choice == 'paper') or (user_choice == 'paper' and comp_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    comp_score = 0
    choices = ['rock', 'paper', 'scissors']
    play_again = True

    print("Welcome to Rock-Paper-Scissors Game!")
    while play_again:
        print("\nChoose: rock, paper, or scissors")
        user_choice = input("Your choice: ").lower()

        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        comp_choice = random.choice(choices)

        print(f"You chose: {user_choice.capitalize()}")
        print(f"Computer chose: {comp_choice.capitalize()}")

        result = determine_winner(user_choice, comp_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            comp_score += 1

        print(f"Score - You: {user_score}  Computer: {comp_score}")

        play = input("Do you want to play again? (yes/no): ")
        play_again = play.lower() == 'yes'

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
