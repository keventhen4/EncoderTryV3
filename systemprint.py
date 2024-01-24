import sys, random, time
from colorsmodule import colortxt


def sprint(txt:str, color="default", fp=False, breakst=False, slpt=0, inpt=False):
  userinpt = None
  #txt is the text to be printed, and slpt is sleeptime (0 if not specified)
  #enter color as number
  print(colortxt(txt="", color=color), end="")
  for i in txt:
#      if color != 'none':
      print(i, end="")
      #sys.stdout.write(i)
#      else:
#        print(i, end="")
      sys.stdout.flush()
      if fp == False:
        time.sleep(random.uniform(0.01, 0.09))
#      time.sleep(random.randint(1, 10) / 100)
  if fp == False:
    time.sleep(slpt)
  if inpt == True:
    print(colortxt(txt="", color="default"), end="")
    userinpt = input()
  if breakst == True:
    print("")
  return userinpt

