from ast import Break, NotIn, Try
import random

while True:
    
    RandomList = ['R','P','S']
# R represent ROCK, S represent SCISSORS, P represent PAPER
    try:
        
        USER = str(input('select randomly from the R,P,S ')) 
        COMPUTER = random.choice(RandomList)
        if USER.upper in RandomList :
            if USER.upper == COMPUTER:
                print('That\'s a tie , try again')
            elif USER.upper =='R' and COMPUTER == 'P':
                print('COMPUTER WINS!!!,YOU LOSE')
                
            elif USER.upper == 'R' and COMPUTER == 'S':
                print('YOU WON!!!, HURRAY')
                
            elif USER.upper == 'P' and COMPUTER == 'R':
                print('YOU WON!!!, HURRAY')
                
            elif USER.upper == 'P' and COMPUTER == 'S':
                print('COMPUTER WINS!!!,YOU LOSE')
                
            elif  USER.upper == 'S' and COMPUTER == 'P':
                print ('YOU WON!!!, HURRAY')
                
            elif  USER.upper == 'S' and COMPUTER == 'R':
                print('COMPUTER WINS!!!,YOU LOSE')
               
        else:
            print('Not amongst our options, Please kindly select from R,P,S')
            continue
            
        

    except (ValueError,TypeError) as error :
        print(error)
    


