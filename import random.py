import random

def describe_game():
    print("🎉 Welcome to the Ultimate Prize Game Show! 🎉")
    print("There are 3 mystery boxes in front of you.")
    print("One box has a GRAND PRIZE 🎁, another has a small prize 🎉, and one is empty 😢.")
    print("Choose wisely and see what you win!\n")

def get_player_choice():
    choice = input("Which box do you choose? (1, 2, or 3): ")
    while choice not in ["1", "2", "3"]:
        choice = input("Invalid choice. Please choose 1, 2, or 3: ")
    return int(choice)

def reveal_prize(player_choice, prizes):
    # Show what was in the chosen box
    selected_prize = prizes[player_choice - 1]
    print("\nYou open the box...")

    if selected_prize == "grand":
        print("🎉 CONGRATULATIONS! You won the GRAND PRIZE!!! 🎁")
        return "win"
    elif selected_prize == "small":
        print("🎉 Nice! You won a small prize. Better luck next time for the big one!")
        return "small"
    else:
        print("😢 Oh no! The box is empty. Better luck next time!")
        return "lose"

def play_game():
    describe_game()
    
    while True:
        # Randomly assign prizes to the boxes
        prizes = ["grand", "small", "empty"]
        random.shuffle(prizes)

        choice = get_player_choice()
        result = reveal_prize(choice, prizes)

        # Ask to play again
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing the Ultimate Prize Game Show! Goodbye! 👋")
            break
        else:
            print("\n--- Let's play again! ---\n")

# Start the game
play_game()
