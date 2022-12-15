import compileall
import os
import random
import string
import sys
import time

banner=""" 
 \033[94m __ _ _ __ ___ (_)_ __ \033[91m ___(_) | ___ __ _   _ _   _ 
\033[94m / _` | '_ ` _ \| | '_  \033[91m|_  / | |/ / '__| | | | | | |
\033[94m| (_| | | | | | | | | | \033[91m|/ /| |   <| |  | |_| | |_| |
\033[94m \__,_|_| |_| |_|_|_| |_\033[91m/___|_|_|\_\_|   \__, |\__, |
 \033[94m                       \033[91m                |___/ |___/  
 \033[0m                                                """
print(banner)

print('Selamat Datang Ke Random Password Generator By aminzikryy')
length = int(input('\nNak Berapa Panjang Password nya? '))

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbols = "!@\#$%&?/"

all = lower + upper + num + symbols
temp = random.sample(all,length)

all = string.ascii_letters + string.digits + string.punctuation

password = "".join(temp)

from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep
print("\b")
print("Loading:")


#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["\033[92m[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")
print ("\033[0mHere is your password :")
print("\b")
print(password)
print("\b")
