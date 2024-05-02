#Importing modules
import time
import sys
import random

def intro():
    print("You are in the Kingdom of Dragons.\nIn front of you, you see two caves.\nIn one cave, the dragon is friendly and will\nshare his treasure with you.\nThe other dragon is hungry and will eat you on sight! ")

def mid():
    print("You approach the cave...",select_cave,"\nA large dragon jumps out in front of you!\nHe opens his jaws and...")

def user():
    global select_cave
    select_cave=input("Cave 1,2,3,4,5 : ")
    return select_cave
    

dead="Gobbles you down!"
win="Greets you before share his treasure!"

while True:
    intro()
    print()
    
    
        
    user()
    try:
        if select_cave.isnumeric()==True and int(select_cave)>0 and int(select_cave)<6 :
                
                
                
                print()
                mid()
                print()
                time.sleep(5)
                result=random.randrange(1,6)
                if result==int(select_cave):
                    print(win)
                else :
                    print(dead)


              
                print()
                    
                ans=input("Do you want to play again? (y/n) ")
                if ans=="n": 
                    exit()
                elif ans=="y":
                    
                    print()
                    #intro()
                    #print()
                    
                    
                
            
                    
    except:
        user()

