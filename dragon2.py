#Importing modules
import time
import sys
import random

#Declaring variables
select_cave=""
dead="Gobbles you down!"
win="Greets you before share his treasure!"


#Defining the intro function
def intro():
    print("You are in the Kingdom of Dragons.\nIn front of you, you see two caves.\nIn one cave, the dragon is friendly and will\nshare his treasure with you.\nThe other dragon is hungry and will eat you on sight! ")

#Defining the mid function
def mid():
    print("You approach the cave...",select_cave,"\nA large dragon jumps out in front of you!\nHe opens his jaws and...")

#Defining the user function
def user():
    global select_cave
    select_cave=input("Cave 1,2,3,4,5 : ")
    return select_cave
    

while True:
    #Calling the intro function
    intro()
    print()
    
    #Calling the user function   
    user()

    #Using exception handling
    try:
        if select_cave.isnumeric()==True and int(select_cave)>0 and int(select_cave)<6 :
                print()
            
                #Calling the mid function
                mid()
                print()

                #Using time.sleep(5) to have a pause of 5 sections to increase the curiosity
                time.sleep(5)

                #Using the random module find the random number from 1 to 5
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
                                    
    except:
        user()

