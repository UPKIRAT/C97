import random

random_number = random.randint(1,10)
tries = 0
user_value = input('''
You and the computer will choose a number from 1 to 10
If you get the same number, you win
Enter you number: ''')
off = 0

if (int(user_value) > int(random_number)):
    off = int(user_value) - int(random_number)
else:
    off = int(random_number) - int(user_value) 

if (int(random_number) == int(user_value)):
    print("You are correct")

if (int(random_number) != int(user_value)):
    tries = tries + 1

if (int(random_number) != int(user_value) & int(tries) == 5):
    print("Game over, you have used up all of your lives")

if (int(random_number) != int(user_value)):
    print("Incorrect! " + "Your were " + str(off) + " off, as the number was " + str(random_number) + ". You have a total of 5 lives and you have already used " + str(tries))