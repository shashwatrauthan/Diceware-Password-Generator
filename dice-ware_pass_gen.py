# Dice-Ware Password Generator   (Python)
# Shashwat Rauthan
# Btech. (CSE) 2019-23
# University Roll No.: 2014458

import random
import csv

# for getting random values from 1-6
def dice_roll():
    return random.choice("123456")

# for getting corrosponding word of dice generated number from wordlist
def find_wordlist(dice):
    csv_file = csv.reader(open('wordlist.csv', "r"), delimiter=",")
    for row in csv_file:
        if row[0] == dice:
            return (row[1])

words = int(input("Enter the number of words you want in password : "))
password = ''
for i in range(words):          #generating words, till number of words user wants
    dice_number = ""
    for j in range(5):          #rolling dice 5 times     #Eg. we get   13567
        dice_number = dice_number + dice_roll()
    word = find_wordlist(dice_number)
    password = password + word + '-'        #words in password are separated by (-)

                                            #clutch-paltry-catalyze-ouch-jurist

password = password[:-1]           #removing last element from password i.e. (-)
print(f"Password is : {password}")
