



def textmsg(msg, waitTime, color, breakstxt):
  global quicktype
  for i in msg:
    if color != False:
      print(colored(i, color), end="")
    #sys.stdout.write(i)
    else:
      print(i, end="")
    sys.stdout.flush()
    time.sleep(waitTime)
  if breakstxt == True:
    print()
    print()
  #textmsg("~ Wonderful!", 0, 'green', False)
  #textmsg("? HeY(y/n)", 0, 'yellow', False)
  #textmsg("! Warning", 0, 'red', False)


def exit():
  textmsg("! I cannot determine what you inputted, but it is not any of the allowed inputs, and so goodbye and a good day to you.", random.uniform(0.01,0.1), 'red', True)
  quit()







textmsg("? Would you like to use Symmetric or Assymmetric Encryption/Decryption(S/A): ", 0, 'yellow', False)
EN_O_DE = input()



if EN_O_DE.upper() == "S":
  textmsg("? Would you like to encrypt or decrypt (E/D): ", 0, 'yellow', False)
  eord = input()

  if eord.upper() == "E":
    textmsg("? Do you have a key, or would you like to generate one (H/G): ", 0, 'yellow', False)
    HaveKey = input()

    if HaveKey.upper() == "H":
      textmsg("? Please enter key:\n", 0, 'yellow', True)
      keytxt = input()
      key = keytxt[2:len(keytxt)]
    elif HaveKey.upper() == "G":
      key = Fernet.generate_key()
    else:
      exit()
    try:
      fernet = Fernet(key)
      textmsg("? Input text to be encrypted:\n", 0, 'yellow', True)
      text = input()
      encMessage = fernet.encrypt(text.encode())
      #textmsg("Key In Bytes:\n\n", 0, 'green', False)
      #textmsg(key, 0, 'green', True)
      textmsg("Key As String:\n\n" + str(key), 0, 'green', True)
      #textmsg("Encrypted Text As Bytes:\n\n", 0, 'green', False)
      #textmsg(encMessage, 0, 'green', True)
      textmsg("Encrypted Text As String:\n\n" + str(encMessage), 0, 'green', False)
    except:
      exit()
  elif eord.upper() == "D":
    textmsg("? Please enter key:\n", 0, 'yellow', True)
    keytxt = input()
    key = keytxt[2:len(keytxt)]
    try:
      fernet = Fernet(key)
      textmsg("? Please input text to be decrypted:\n", 0, 'yellow', True)
      texttxt = input()
      text = texttxt[2:len(texttxt)]
      decMessage = fernet.decrypt(bytes(text,'utf-8')).decode()
      textmsg("Key:\n\n" + str(key), 0, 'green', True)
      textmsg("Decrypted Text:\n\n" + str(decMessage), 0, 'green', False)
    except:
      exit()
  else:
    exit()


elif EN_O_DE.upper() == "A":
  
  textmsg("~ Also Very Wonderful!", 0, 'green', True)


else:
  exit()