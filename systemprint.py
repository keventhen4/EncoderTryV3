import sys, random, time
from colorsmodule import colortxt

def systemprint(txt:str, color="none", quicktype=False, breakst=False, slpt=0, inpt=False):
  #txt is the text to be printed, and slpt is sleeptime (0 if not specified)
  #enter color as number
  for i in txt:
      if color != 'none':
        print(colortxt(i, color), end="")
      #sys.stdout.write(i)
      else:
        print(i, end="")
      sys.stdout.flush()
      if quicktype == False:
        time.sleep(random.uniform(0.01, 0.09))
#      time.sleep(random.randint(1, 10) / 100)
  if quicktype == False:
    time.sleep(slpt)
  if inpt == True:
    input()
  if breakst == True:
    print("")