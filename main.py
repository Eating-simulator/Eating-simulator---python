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
def logo():
  print('''
   _______     ___   .___________. __  .__   __.   _______         _______. __  .___  ___.  __    __   __          ___   .___________.  ______   .______      
  |   ____|   /   \  |           ||  | |  \ |  |  /  _____|       /       ||  | |   \/   | |  |  |  | |  |        /   \  |           | /  __  \  |   _  \     
  |  |__     /  ^  \ `---|  |----`|  | |   \|  | |  |  __        |   (----`|  | |  \  /  | |  |  |  | |  |       /  ^  \ `---|  |----`|  |  |  | |  |_)  |    
  |   __|   /  /_\  \    |  |     |  | |  . `  | |  | |_ |        \   \    |  | |  |\/|  | |  |  |  | |  |      /  /_\  \    |  |     |  |  |  | |      /     
  |  |____ /  _____  \   |  |     |  | |  |\   | |  |__| |    .----)   |   |  | |  |  |  | |  `--'  | |  `----./  _____  \   |  |     |  `--'  | |  |\  \----.
  |_______/__/     \__\  |__|     |__| |__| \__|  \______|    |_______/    |__| |__|  |__|  \______/  |_______/__/     \__\  |__|      \______/  | _| `._____|                     
  ''')

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
    logo()
    print(f'''
    
    You have {money} money.
    You have {calories} calories in your body.


    Press e to go to the store and eat something

    Press j to get a job

    Type exit to get to go to main page
  ''')
  elif job != "":
      clear()
      logo()
      print(f'''
      You have {money} money.
      You have {calories} calories in your body.
      Your job is {job}.

      Press e to go to the store and eat something

      Press j to work ({job})

      Type exit to go to main page
  ''')
  myinput = input("What would you like to do?")
  if myinput == "e":
    clear()
    logo()
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
    logo()
    print('''
                .---.            
               |   '.|  __       
               | ___.--'  )      
             _.-'_` _%%%_/       
          .-'%%% a: a %%%        
              %%  L   %%_        
              _%\\'=' |  /-.__    
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
           \\\\ __..--""        
           calories: 300
           money: 5.00$
           press "P" to buy
    ''')
    myinput = input("What would you like to buy?")
    if myinput == "p":
      print("You bought pizza")
      money = money - 5
      calories = calories + 300
      print("Press enter to continue.")
      input()
  elif myinput == "j":
    clear()
    logo()
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
          print("Press enter to continue.")
          input()
        elif randomnumber == 2:
          print("They finally assign you a job. it's babysitting!!")
          time.sleep(3)
          print("The salary is 30 dollars a baby. not too shabby!")
          jobpicked = True
          job = "Babysitting"
          print("Press enter to continue.")
          input()
        elif randomnumber == 3:
          print("They finally assign you a job. it's lawnmowing!!")
          time.sleep(3)
          print("The salary is 25 dollars a lawn. not too shabby!")
          jobpicked = True
          job = "Lawnmowing"
          print("Press enter to continue.")
          input()
    elif jobpicked == True:
      if job == "Pizza delivery":
        print("You deliver pizza")
        time.sleep(4)
        print("All done! you delivered pizza and gained 20 dollars.")
        money = money + 20
        print("Press enter to continue.")
        input()
      elif job == "Babysitting":
        print("You went babysitting!")
        time.sleep(4)
        print("You completed babysitting and gained 30 dollars!")
        money = money + 30
        print("Press enter to continue.")
        input()
      elif job == "Lawnmowing":
        print("You start to mow someone's lawn")
        time.sleep(4)
        print("You complete lawnmowing and earned 25 dollars!")
        money = money + 25
        print("Press enter to continue.")
        input()
  elif myinput == "exit":
    clear()
    logo()
    print('''
    .___________. __    __   _______    .___  ___.  _______ .__   __.  __    __  
    |           ||  |  |  | |   ____|   |   \/   | |   ____||  \ |  | |  |  |  | 
    `---|  |----`|  |__|  | |  |__      |  \  /  | |  |__   |   \|  | |  |  |  | 
        |  |     |   __   | |   __|     |  |\/|  | |   __|  |  . `  | |  |  |  | 
        |  |     |  |  |  | |  |____    |  |  |  | |  |____ |  |\   | |  `--'  | 
        |__|     |__|  |__| |_______|   |__|  |__| |_______||__| \__|  \______/  
    
    Press 1 for settings

    Press 2 for credits

    Press 3 To get link for real eating simulator
    ''')
    myinput = input()
    if myinput == "1":
      clear()
      logo()
      print(f'''
           _______. _______ .___________.___________. __  .__   __.   _______      _______.
          /       ||   ____||           |           ||  | |  \ |  |  /  _____|    /       |
          |  (----`|  |__   `---|  |----`---|  |----`|  | |   \|  | |  |  __     |   (----`
          \   \    |   __|      |  |        |  |     |  | |  . `  | |  | |_ |     \   \    
      .----)   |   |  |____     |  |        |  |     |  | |  |\   | |  |__| | .----)   |   
      |_______/    |_______|    |__|        |__|     |__| |__| \__|  \______| |_______/    

      Your current settings are: 

      Job: {job} (Can't be changed)
      Money: {money} 
      Calories: {calories}
      ''')
      print("Press enter or return to exit.")
      input()
    elif myinput == "2":
      clear()
      logo()
      print('''
        ______ .______       _______  _______   __  .___________.    _______.
       /      ||   _  \     |   ____||       \ |  | |           |   /       |
      |  ,----'|  |_)  |    |  |__   |  .--.  ||  | `---|  |----`  |   (----`
      |  |     |      /     |   __|  |  |  |  ||  |     |  |        \   \    
      |  `----.|  |\  \----.|  |____ |  '--'  ||  |     |  |    .----)   |   
       \______|| _| `._____||_______||_______/ |__|     |__|    |_______/    

       For python ES:
       ch1ck3n 
       technodoggo

       For HTML5 ES:
       ch1ck3n
       technodoggo
       ID7
      
      ''')
      print("To go back press enter")
      input()
    elif myinput == "3":
      clear()
      logo()
      print('''
       __    __  .___________..___  ___.  __       _____       _______      ___      .___  ___.  _______ 
      |  |  |  | |           ||   \/   | |  |     | ____|     /  _____|    /   \     |   \/   | |   ____|
      |  |__|  | `---|  |----`|  \  /  | |  |     | |__      |  |  __     /  ^  \    |  \  /  | |  |__   
      |   __   |     |  |     |  |\/|  | |  |     |___ \     |  | |_ |   /  /_\  \   |  |\/|  | |   __|  
      |  |  |  |     |  |     |  |  |  | |  `----. ___) |    |  |__| |  /  _____  \  |  |  |  | |  |____ 
      |__|  |__|     |__|     |__|  |__| |_______||____/      \______| /__/     \__\ |__|  |__| |_______|
      
      
      ''')
      print("Do you really need the link?")
      time.sleep(3)
      print("... yes. you do.")
      time.sleep(3)
      print("fine.")
      time.sleep(2)
      clear()
      logo()
      print('''
       __    __  .___________..___  ___.  __       _____       _______      ___      .___  ___.  _______ 
      |  |  |  | |           ||   \/   | |  |     | ____|     /  _____|    /   \     |   \/   | |   ____|
      |  |__|  | `---|  |----`|  \  /  | |  |     | |__      |  |  __     /  ^  \    |  \  /  | |  |__   
      |   __   |     |  |     |  |\/|  | |  |     |___ \     |  | |_ |   /  /_\  \   |  |\/|  | |   __|  
      |  |  |  |     |  |     |  |  |  | |  `----. ___) |    |  |__| |  /  _____  \  |  |  |  | |  |____ 
      |__|  |__|     |__|     |__|  |__| |_______||____/      \______| /__/     \__\ |__|  |__| |_______|
      
      
      ''')
      print("https://eating-simulator.github.io/")
      print("Press enter to continue.")
      input()


      
        

