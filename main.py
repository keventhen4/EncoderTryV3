import sys, time, random, os, rsa
from cryptography.fernet import Fernet
from colorsmodule import colortxt
from systemprint import sprint
import pyperclip3 as pc


prg = open("code.py", "r")
exec(prg.read())


prg.close()
time.sleep(10)
os.system('clear')