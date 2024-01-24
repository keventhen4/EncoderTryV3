def clrcmd(code):
  return f"\33[{code}m"

txttable = {
  "default": 0,
  "black": 30,
  "red": 31,
  "green": 32,
  "yellow": 33,
  "blue": 34,
  "purple": 35,
  "cyan": 36,
  "white": 37
}

def colortxt(txt:str, color:str):
  return clrcmd(str(txttable[color.lower()])) + txt