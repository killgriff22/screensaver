import time
import os
import random
os.system("clear")
print("\x1b[32m")
with open("samples.txt","r") as f:
    samples = f.readlines()
while True:
    ans = input("input 1 for hacker code\ninput 2 for matrix hacking\n>>")
    os.system("clear")
    if ans == "1":
        try:
            while True:
                sample = random.choice(samples)
                for letter in sample:
                    time.sleep(0.01)
                    print(letter,end="",flush=True)
                time.sleep(0.05)
        except KeyboardInterrupt:
            print("\x1b[0m")
            exit()
    elif ans == "2":
        try:
            while True:
                line=""
                for _ in range(os.get_terminal_size().columns):
                    choice = int(random.random()*2//1)
                    if not _%4 == 0:
                        line+=" "
                    elif _%4 == 0:
                        line += str(choice)
                print(line,end="")
        except KeyboardInterrupt:
            print("\x1b[0m")
            exit()
    elif ans == "" or not ans in ["1","2"]:
        pass