
import random as rand

def game(n):
    guess=''
    win=0
    draw=0
    loose=0
    wrong_entry=0
    name=input('Enter player name: ')
    for i in range(n):
        random_number=rand.randint(1,3)
        if random_number==1:
          random_number='r'
        elif random_number==2:
            random_number='p'
        elif random_number==3:
            random_number='s'
        guess=input("Enter your choice: ").lower()
        if guess=='r' or guess=='p' or guess=='s':
            print(f"Compter entry is {random_number}")
            if(guess==random_number):
                print("It's a draw")
                draw+=1
            else:
                if(guess=='r'):  
                    if(random_number=='p'):
                        print("Computer win")
                        loose+=1
                    elif(random_number=='s'):
                        print(f'{name} win')
                        win+=1
                elif(guess=='p'):
                    if(random_number=='r'):
                        print(f'{name} win')
                        win+=1
                    elif(random_number=='s'):
                        print('Computer win')
                        loose+=1
                elif(guess=='s'):
                    if(random_number=='r'):
                        print('Computer win')
                        loose+=1
                    elif(random_number=='p'):
                        print(f'{name} win')
                        win+=1
        else:
            print('correct your entry')
            wrong_entry+=1
    
    print(f'You win: {win}',)
    print(f'You Loose: {loose}',)
    print(f'Draw: {draw}',)
    print(f'Wrong input: {wrong_entry}')
                
game(10)
