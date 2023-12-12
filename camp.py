import time
import os
global charactername
def camp():
    print('''Your in camp. There are 6 things you can do. What do you do?
    [1] EXPLORE
    [2] REST
    [3] GO TO STORE
    [4] OPEN INVENTORY
    [5] PREPARE
    [6] QUIT GAME
    ''')
    command = input("Enter command: ")
    if command == "1":
        print("You go out to explore...")
    elif command == "2":
        print("You rest.")