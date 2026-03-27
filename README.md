# Dice-Game-python
To develop a Python-based dice game where the player competes against the computer, and  the first to reach a total score of 30 wins. 
🎲 Dice Rolling Game in Python

A simple and fun Dice Rolling Game built using Python where the player competes against the computer to reach a target score.

🚀 Features
🎯 Target Score Gameplay
First player to reach 30 points wins
🎮 Turn-Based System
Player and computer take turns rolling the dice
🎲 Random Dice Rolls
Uses Python’s random module for realistic dice outcomes
💻 Computer Opponent
Play against an automated system
🧠 Simple Game Logic
Great for beginners to understand loops and functions
🛠️ Tech Used
Python
Random Module
Command Line Interface (CLI)
📸 Sample Output
🎯 First to reach 30 wins!

--- Your Turn ---
Press Enter to roll dice...
You rolled: 5
Your Total Score: 5

--- Computer Turn ---
Computer rolled: 3
Computer Total Score: 3
💻 Full Code
import random 

def roll_dice(): 
    return random.randint(1, 6) 

def player_turn(): 
    input("Press Enter to roll dice...") 
    roll = roll_dice() 
    print(f"You rolled: {roll}") 
    return roll 

def computer_turn(): 
    roll = roll_dice() 
    print(f"Computer rolled: {roll}") 
    return roll 

def game(): 
    player_score = 0 
    computer_score = 0 
    target = 30 

    print("🎯 First to reach 30 wins!\n") 

    while player_score < target and computer_score < target: 
        print("\n--- Your Turn ---") 
        player_score += player_turn() 
        print(f"Your Total Score: {player_score}") 

        if player_score >= target: 
            break 

        print("\n--- Computer Turn ---") 
        computer_score += computer_turn() 
        print(f"Computer Total Score: {computer_score}") 

    print("\n🏁 Game Over!") 

    if player_score > computer_score: 
        print("🎉 You Win!") 
    else: 
        print("💻 Computer Wins!") 

game()
<img width="1918" height="837" alt="Screenshot 2026-03-27 140055" src="https://github.com/user-attachments/assets/8d641d24-f3ee-4f26-8625-81d2ecce44d4" />

▶️ How to Run
Install Python (if not already installed)
Save the file as dice_game.py
Run the program:
python dice_game.py
📈 Future Improvements
Add multiplayer mode
Add GUI using Tkinter
Add difficulty levels
Store high scores
Add animations for dice rolling
🤝 Contributing

Feel free to fork this repository and enhance the game. Contributions are welcome!

⭐ Support

If you like this project, don’t forget to give it a ⭐ on GitHub!
