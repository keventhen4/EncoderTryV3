import sys, time, random, os, rsa
from termcolor import colored
from cryptography.fernet import Fernet
from colorsmodule import colortxt
from systemprint import systemprint


prg = open("code.py", "r")
exec(prg.read())


#prg.close()
time.sleep(10)
os.system('clear')