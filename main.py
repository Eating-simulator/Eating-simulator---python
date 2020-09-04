#Best to run repl in full screen!
print("To get better ASCII art play game in full screen.")
from time import sleep as s
from sys import stdout as sw
import time
from replit import clear
import random
def typrint(text, speed):
   for letter in text:
    s(float(speed))
    sw.write(letter)
    sw.flush()
money = 100
calories = 300
gameover = False
myinput = "yeet"
jobpicked = False
randomnumber = 4 
job = ""
time.sleep(3)
clear()
time.sleep(2)
print("This is a game")
time.sleep(2)
print("Also a story")
time.sleep(3)
print("Welcome to")
time.sleep(2)
print('''
 _______     ___   .___________. __  .__   __.   _______         _______. __  .___  ___.  __    __   __          ___   .___________.  ______   .______      
|   ____|   /   \  |           ||  | |  \ |  |  /  _____|       /       ||  | |   \/   | |  |  |  | |  |        /   \  |           | /  __  \  |   _  \     
|  |__     /  ^  \ `---|  |----`|  | |   \|  | |  |  __        |   (----`|  | |  \  /  | |  |  |  | |  |       /  ^  \ `---|  |----`|  |  |  | |  |_)  |    
|   __|   /  /_\  \    |  |     |  | |  . `  | |  | |_ |        \   \    |  | |  |\/|  | |  |  |  | |  |      /  /_\  \    |  |     |  |  |  | |      /     
|  |____ /  _____  \   |  |     |  | |  |\   | |  |__| |    .----)   |   |  | |  |  |  | |  `--'  | |  `----./  _____  \   |  |     |  `--'  | |  |\  \----.
|_______/__/     \__\  |__|     |__| |__| \__|  \______|    |_______/    |__| |__|  |__|  \______/  |_______/__/     \__\  |__|      \______/  | _| `._____|                     
''')
time.sleep(5)
typrint("This is a game where you live a normal life.", 0.05)
time.sleep(5)
clear()
while gameover != True:
  if job == "":
    clear()
    print(f'''
    _______     ___   .___________. __  .__   __.   _______         _______. __  .___  ___.  __    __   __          ___   .___________.  ______   .______      
    |   ____|   /   \  |           ||  | |  \ |  |  /  _____|       /       ||  | |   \/   | |  |  |  | |  |        /   \  |           | /  __  \  |   _  \     
    |  |__     /  ^  \ `---|  |----`|  | |   \|  | |  |  __        |   (----`|  | |  \  /  | |  |  |  | |  |       /  ^  \ `---|  |----`|  |  |  | |  |_)  |    
    |   __|   /  /_\  \    |  |     |  | |  . `  | |  | |_ |        \   \    |  | |  |\/|  | |  |  |  | |  |      /  /_\  \    |  |     |  |  |  | |      /     
    |  |____ /  _____  \   |  |     |  | |  |\   | |  |__| |    .----)   |   |  | |  |  |  | |  `--'  | |  `----./  _____  \   |  |     |  `--'  | |  |\  \----.
    |_______/__/     \__\  |__|     |__| |__| \__|  \______|    |_______/    |__| |__|  |__|  \______/  |_______/__/     \__\  |__|      \______/  | _| `._____|  
    You have {money} money.
    You have {calories} calories in your body.


    Press e to go to the store and eat something

    Press j to get a job

    Type exit to get to go to main page
  ''')
  elif job != "":
      clear()
      print(f'''
      You have {money} money.
      You have {calories} calories in your body.
      Your job is {job}.

      Press e to go to the store and eat something

      Press j to get a job

      Type exit to go to main page
  ''')
  myinput = input("What would you like to do?")
  if myinput == "e":
    print("You entered the store")
    time.sleep(3)
    print("You see somebody")
    time.sleep(4)
    print("He looks like a cowboy")
    time.sleep(2)
    print("He probably is the merchant")
    time.sleep(3)
    print("Yup, he is.")
    time.sleep(5)
    clear()
    print('''
                .---.            
               |   '.|  __       
               | ___.--'  )      
             _.-'_` _%%%_/       
          .-'%%% a: a %%%        
              %%  L   %%_        
              _%\'=' |  /-.__    
           .-' / )--' #/     '\  
          /'  /  /---'(    :   \ 
         /   |  /( /|##|  \     |
        /   ||# | / | /|   \    \
        
        |   ||: | o  |#|   |  / |
        |   ||  / I  |:/  /   |/ 
        |   ||  | o   /  /    /  
        |   \|  | I  |. /    /   
         \  /|##| o  |.|    /    
          \/ \::|/\_ /  ---'|    
           \ |\ |    |     :\    
           | |  /     \...' |    
           | |# |/\    \    |    
           | | :|  |    |   |    
           | |  |  |    |   |   
           Arr, i'm the shopkeeper.
           Buy me' food! they' good!

           Here' arr me products.

           1. pizza
           // ""--.._         
           ||  (_)  _ "-._    
           ||    _ (_)    '-. 
           ||   (_)   __..-'  
           \\ __..--""        
           calories: 300
           money: 5.00$
           press "P" to buy
    ''')
    myinput = input("What would you like to buy?")
    if myinput == "p":
      print("You bought pizza")
      money = money - 5
      calories = calories + 300
  elif myinput == "j":
    if jobpicked == False:
        print("You go the the job place")
        time.sleep(5)
        print("They start deciding what job you should do.")
        time.sleep(3)
        print("This is going to take a while.")
        time.sleep(6)
        print("Waiting...")
        time.sleep(3)
        print("Waiting......")
        time.sleep(5)
        print("How much time is this going to take them?")
        randomnumber = random.randint(1, 3)
        if randomnumber == 1:
          print("They finally assign you a job. it's pizza delivery!")
          time.sleep(3)
          print("The salary is 20 dollars a pizza. that's 4 pizzas!")
          jobpicked = True
          job = "Pizza delivery"
        elif randomnumber == 2:
          print("They finally assign you a job. it's babysitting!!")
          time.sleep(3)
          print("The salary is 30 dollars a baby. not too shabby!")
          jobpicked = True
          job = "Babysitting"
        elif randomnumber == 3:
          print("They finally assign you a job. it's lawnmowing!!")
          time.sleep(3)
          print("The salary is 25 dollars a lawn. not too shabby!")
          jobpicked = True
          job = "Lawnmowing"
    elif jobpicked == True:
      if job == "Pizza delivery":
        print("You deliver pizza")
        time.sleep(4)
        print("All done! you delivered pizza and gained 20 dollars.")
        money = money + 20
      elif job == "Babysitting":
        print("You went babysitting!")
        time.sleep(4)
        print("You completed babysitting and gained 30 dollars!")
        money = money + 30
      elif job == "Lawnmowing":
        print("You start to mow someone's lawn")
        time.sleep(4)
        print("You complete lawnmowing and earned 25 dollars!")
        money = money + 5


      
        

