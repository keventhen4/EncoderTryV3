colorcommand = "\033["
styletable = {
  "none": 0,
  "bold": 1,
  "underline": 2,
  "negative1": 3,
  "negative2": 5
}
txttable = {
  "black": 30,
  "red": 31,
  "green": 32,
  "yellow": 33,
  "blue": 34,
  "purple": 35,
  "cyan": 36,
  "white": 37
}
bgtable = {
  "black": 40,
  "red": 41,
  "green": 42,
  "yellow": 43,
  "blue": 44,
  "purple": 45,
  "cyan": 46,
  "white": 47
}

def colortxt(txt:str, color:str, style="none", bg="black"):
  print(colorcommand + str(styletable[style.lower()]) + ";" + str(txttable[color.lower()]) + ";" +str(bgtable[bg.lower()]) + "m" + txt)