'''Assignment: Create Rock Paper Scissors Game'''
'''Programmer: Sachorra Douglas'''
'''Date: October 30th, 2024'''

print("Made by Sachorra Douglas. Visit https://www.linkedin.com/in/sachorradouglas/ to stay connected ;)")
lose = ("You Lose :(")
win = ("You Win :)")
lives = 5
score = 0
drew = 0
computer_lives = 7

while True:
  print("To begin fill in the below information.")
  username = input("Please enter your username:")
  password = input("Please enter your password.")
  print("Access Granted")
  print("Welcome to the game")
  rules = input("Would you like to see the rules?")
  if rules == "yes":
    print("Rock loses to paper, paper loses to scissors, scissors loses to rock")
    print("Rock beats scissors, paper beats rock, scissors beats paper")
    print("If you win you get a point, if you lose you lose a life")
    print("You start with 5 lives")
    print("If you draw you get no points")
    print("If you win 3 rounds you win")
    print("If you lose all your lives you lose")
    print("To see your score and lives type score")
    print("To see the computers score and lives type computer")
    print("To see the amount of draws type draws")
    print("To see the amount of wins type wins")
    print("To see the amount of losses type losses")
  
  while True:
    rps = input("Rock, Paper, Scissors... Say SHOOT!")
    import random
    computer = ("rock", "paper", "scissors")
    computer = random.choice(computer)
  #rock if statements
    if rps == "rock" and computer == "paper":
        print("The computer choose", computer)
        print("")
        print("You lose")
        print("")
        print("")
        lives = lives - 1
        print("You have", lives, "lives left")
    if rps == "rock" and computer == "scissors":
        print("The computer choose", computer)
        print("")
        print(win)
        print("")
        print("")
        score+=1
  #paper if statements
    if rps == "paper" and computer == "rock":
        print("The computer choose", computer)
        print("")
        print(win)
        computer_lives -= 1
        print("")
        print("")
        score+=1
    if rps == "paper" and computer == "scissors":
        print("The computer choose", computer)
        print("")
        print(lose)
        print("")
        print("")
        lives-=1
  #scissors if statements
    if rps == "scissors" and computer == "paper": 
        print("The computer choose", computer)
        print("")
        print(win)
        computer_lives -= 1
        print("")
        print("")
        score+=1
    if rps == "scissors" and computer == "rock":
        print("The computer choose", computer)
        print("")
        print(lose)
        print("")
        print("")
        lives-=1
  #duplicates
    if rps == "rock" and computer == "rock":
        print("The computer choose", computer)
        print("")
        print("Draw")
        print("")
        print("")
        drew+=1
    if rps == "paper" and computer == "paper":
        print("The computer choose", computer)
        print("")
        print("Draw")
        print("")
        print("")
        drew+=1
    if rps == "scissors" and computer == "scissors":
        print("The computer choose", computer)
        print("")
        print("Draw")
        print("")
        print("")
        drew+=1
  #system
    if rps == "rules":
        print("Rock loses to paper, paper loses to scissors, scissors loses to rock")
        print("Rock beats scissors, paper beats rock, scissors beats paper")
        print("If you win you get a point, if you lose you lose a life")
        print("You start with 5 lives")
        print("If you draw you get no points")
        print("If you win 3 rounds you win")
        print("If you lose all your lives you lose")
        print("To see your score and lives type score")
        print("To see the computers score and lives type computer")
        print("To see the amount of draws type draws")
        print("To see the amount of wins type wins")
        print("To see the amount of losses type losses")
    if rps == "display lives":
        print(lives)
    if rps == "display score":
        print(score)
    if rps == "display draws":
        print(draw)
  #lives
    lives = 3  # Example initial value for lives

    if lives == 0 or rps == "test":
        rematch = input("Rematch? (yes/no)")
        if rematch == "yes":
            lives = 5  # Reset lives or other game variable
            score = 0  # Reset score or other game variable
            drew = 0
            computer_lives = 7
            print("Game restarted!")
            rps = input("Rock, Paper, Scissors... Say SHOOT!")
        elif rematch == "no":
            print("Thanks for playing!")
        else:
            print("Please type 'yes' or 'no'.")

    
