import time
import os
import random
os.system("clear")
print("\x1b[32m")
with open("samples.txt","r") as f:
    samples = f.readlines()
try:
    while True:
        sample = random.choice(samples)
        for letter in sample:
            time.sleep(0.01)
            print(letter,end="",flush=True)
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\x1b[0m")