import random

# ===================== ROLL FUNCTION =====================
def roll_dice():
    return random.randint(1, 6)

# ===================== PLAYER TURN =====================
def player_turn():
    turn_score = 0
    
    while True:
        choice = input("Roll or Hold? (r/h): ").lower()
        
        if choice == 'r':
            roll = roll_dice()
            print(f"You rolled: {roll}")
            
            if roll == 1:
                print("💥 You lost your turn points!")
                return 0
            else:
                turn_score += roll
                
                # BONUS RULE
                if roll == 6:
                    print("🔥 Bonus +5 points!")
                    turn_score += 5
                    
                print(f"Turn Score: {turn_score}")
        
        elif choice == 'h':
            return turn_score
        
        else:
            print("Invalid choice! Try again.")

# ===================== COMPUTER TURN =====================
def computer_turn():
    turn_score = 0
    
    while turn_score < 10:  # simple strategy
        roll = roll_dice()
        print(f"Computer rolled: {roll}")
        
        if roll == 1:
            print("💥 Computer lost turn points!")
            return 0
        else:
            turn_score += roll
            
            if roll == 6:
                print("🔥 Computer bonus +5!")
                turn_score += 5
    
    print("Computer holds.")
    return turn_score

# ===================== GAME FUNCTION =====================
def game():
    player_score = 0
    computer_score = 0
    target = 30
    
    print("🎯 First to reach 30 wins!\n")
    
    while player_score < target and computer_score < target:
        
        # PLAYER TURN
        print("\n--- Your Turn ---")
        player_score += player_turn()
        print(f"Your Total Score: {player_score}")
        
        if player_score >= target:
            break
        
        # COMPUTER TURN
        print("\n--- Computer Turn ---")
        computer_score += computer_turn()
        print(f"Computer Total Score: {computer_score}")
    
    # RESULT
    print("\n🏁 Game Over!")
    if player_score >= target:
        print("🎉 You Win!")
    else:
        print("💻 Computer Wins!")

# ===================== START GAME =====================
game()
