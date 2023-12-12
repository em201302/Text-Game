import time
import os
global charactername
print("Welcome to Text-Game! An RPG.")
print("What is your character's name?")
charactername = input("Enter name: ")
charactername = charactername.capitalize()
os.system('clear')
print(charactername + " is a very good name! Well " + charactername + ", Let's get started!")
