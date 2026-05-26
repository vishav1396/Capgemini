import random

def play_game():
    options = ["Stone", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    print("\n--- Stone-Paper-Scissors ---")
    user_choice = input("Enter your choice (Stone/Paper/Scissors): ").capitalize()


    if user_choice not in options:
        print("❌ Invalid input! Please enter Stone, Paper, or Scissors.")
        return  

    print(f"Computer chose: {computer_choice}")

    # Win/Loss Logic
    if user_choice == computer_choice:
        print("🤝 It's a Tie!")
    elif (user_choice == "Stone" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Stone") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        print("🎉 You Win!")
    else:
        print("💀 Computer Wins!")


while True:
    play_game()
    if input("\nPlay again? (y/n): ").lower() != 'y':
        break
        
print("Thanks for playing! Goodbye!")
