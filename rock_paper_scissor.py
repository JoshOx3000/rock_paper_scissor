import random  #import random


def intro():
    print("Welcome 😊 to the game of Rock, Paper, Scissor")
    print("=========================================")
    print("In this game, you can choose:")
    print(" - 'r' for Rock")
    print(" - 'p' for Paper")
    print(" - 's' for Scissors")
    print("To exit the game, type 'q'. Let's see who wins!\n")
    






#input_check function to check if user choice is valid and will say in a while loop til condition is met 
def input_check(choice):
    while True:
        if choice == 'r' or choice == 'p' or choice == 's':
            
            break
        elif choice == 'q':
            print('goodbye 👋😢')
            break
        else:
            print("You enter an invalid choice, Enter 'r' for rock, 'p' for paper, 's' for scissor or 'q' to quit")
            choice = input('Enter your choice: ')
    return choice

#used to determine the winner, argument, cpu/player choice and  return scores
def winner(player_choice, cpu_score, player_score):
    choices= ['r', 'p', 's']
    cpu_choice = random.choice(choices)
    
    if cpu_choice == 'r' and player_choice == 'p':
        print('Computer chose: ', cpu_choice)
        print('You chose: ', player_choice)
        print('You won 😊, CPU lost 😞 ')
        player_score +=1
        cpu_score += 0
        print(f'CPU Score = {cpu_score}')
        print(f'Your Score = {player_score}')
        return player_score, cpu_score
    elif cpu_choice == 's' and player_choice == 'r':
        print('Computer chose: ', cpu_choice)
        print('You chose: ', player_choice)
        print('You won 😊, CPU lost 😞 ')
        player_score +=1
        cpu_score += 0
        print(f'CPU Score = {cpu_score}')
        print(f'Your Score = {player_score}')
        return player_score, cpu_score
    elif cpu_choice == 'p' and player_choice == 's':
        print('Computer chose: ', cpu_choice)
        print('You chose: ', player_choice)
        print('You won 😊, CPU lost 😞 ')
        player_score +=1
        cpu_score += 0
        print(f'CPU Score = {cpu_score}')
        print(f'Your Score = {player_score}')
        return player_score, cpu_score
        
       
    elif player_choice == 'r' and cpu_choice == 'p':
        print('Computer chose: ', cpu_choice)
        print('You chose: ', player_choice)
        print('CPU won 😊, You lost 😞 ')
        player_score +=0
        cpu_score +=1
        print(f'CPU Score = {cpu_score}')
        print(f'Your Score = {player_score}')
        return player_score, cpu_score
    elif player_choice == 's' and cpu_choice == 'r':
        print('Computer chose: ', cpu_choice)
        print('You chose: ', player_choice)
        print('CPU won 😊, You lost 😞 ')
        player_score +=0
        cpu_score +=1
        print(f'CPU Score = {cpu_score}')
        print(f'Your Score = {player_score}')
        return player_score, cpu_score
    elif player_choice == 'p' and cpu_choice == 's':
        print('Computer chose: ', cpu_choice)
        print('You chose: ', player_choice)
        print('CPU won 😊, You lost 😞 ')
        print('\n')
        player_score +=0
        cpu_score +=1
        print(f'CPU Score = {cpu_score}')
        print(f'Your Score = {player_score}')
        print('')
        return player_score, cpu_score
    elif player_choice == cpu_choice:
        print('Tied, now winners') 
        print(f'CPU Score = {cpu_score}')
        print(f'Your Score = {player_score}')
        return player_score, cpu_score

def play_game():
    player_score = 0 #inital player score
    cpu_score = 0  #initial cpu score
    intro() #call intro function to display to user
    
    # input_check(player_choice)
    # winner(player_choice, cpu_score, player_score)
    
    while True:
        player_choice = input('Enter your choice: ').lower()
        player_choice = input_check(player_choice)
        cpu_score, player_score = winner(player_choice, cpu_score, player_score)
        
        play_again = input('Do you want to play again? yes or no ').lower()
        if play_again != 'yes':
            print("Thanks for playing with me! Goodbye 😊")
            break
    
    




#call play game function to run game
play_game()

 
     


