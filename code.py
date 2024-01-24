import sys, time, random, os, rsa
from cryptography.fernet import Fernet
from colorsmodule import colortxt
from systemprint import *
from systemprint import sprint



def exit():
  chance = random.randint(1,100)
  if chance < 98:
    sprint(txt="! Something went wrong", color='red', fp=fp)
  elif chance == 99:
    sprint(txt="! ???", color='red', fp=fp)
  elif chance == 100:
    sprint(txt="? What is your address: ", color='red', inpt=True, fp=fp)
    sprint(txt="! I know your address now", color='red', fp=fp)
  quit()



fastprompt = sprint(txt="? Would you like to use fast prompting (Y/N): ", color="yellow", inpt=True)
if fastprompt.upper() == "Y":
  fp=True
elif fastprompt.upper() == "N":
  fp=False
else:
  exit()

userinpt = sprint(txt="? Would you like to use Symmetric or Assymmetric Encryption/Decryption (S/A): ", color="yellow", inpt=True, fp=fp)

if userinpt.upper() == "S":
  eord = sprint(txt="? Would you like to encrypt or decrypt (E/D): ", color='yellow', inpt=True, fp=fp)

  if eord.upper() == "E":
    HaveKey = sprint(txt="? Do you have a key, or would you like to generate one (H/G): ", color='yellow', inpt=True, fp=fp)

    if HaveKey.upper() == "H":
      keytxt = sprint(txt="? Please enter key:\n", color='yellow', inpt=True, fp=fp)
      key = keytxt
    elif HaveKey.upper() == "G":
      key = Fernet.generate_key()
    else:
      exit()
    try:
      fernet = Fernet(key)
      fernet.encrypt("testtext".encode())
    except:
      try:
        fernet = Fernet(key[2:len(key)])
        fernet.encrypt("testtext".encode())
      except:
        exit()
    text = sprint(txt="? Input text to be encrypted:\n", color='yellow', inpt=True, fp=fp)
    encMessage = fernet.encrypt(text.encode())
    #textmsg("Key In Bytes:\n\n", 0, 'green', False)
    #textmsg(key, 0, 'green', True)
    sprint(txt=f"Key:\v{str(key)[2:len(key)]}\n", color='green', fp=fp)
    #textmsg("Encrypted Text As Bytes:\n\n", 0, 'green', False)
    #textmsg(encMessage, 0, 'green', True)
    sprint(txt=f"Encrypted Text:\v{str(encMessage)[2:len(key)]}", color='green', fp=fp)
  elif eord.upper() == "D":
    key = sprint(txt="? Please enter key:\n", color='yellow', inpt=True, fp=fp)
    try:
      fernet = Fernet(key)
      fernet.encrypt("testtext".encode())
    except:
      try:
        key = keytxt[2:len(keytxt)]
        fernet = Fernet(key)
        fernet.encrpy("testtext".encode())
      except:
        exit()
    texttxt = sprint(txt="? Please input text to be decrypted:\n", color='yellow', inpt=True, fp=fp)
    text = texttxt
    decMessage = fernet.decrypt(bytes(text,'utf-8')).decode()
    sprint(txt=f"Key:\v{str(key)}\n", color='green')
    sprint(txt=f"Decrypted Text:\v{str(decMessage)}", color='green', fp=fp)

  else:
    exit()


elif userinpt.upper() == "A":
  eord = sprint(txt="? Would you like to encrypt or decrypt (E/D): ", color='yellow', inpt=True, fp=fp)
  if eord.upper() == "E":
    HaveKey = sprint(txt="? Do you have a public key, or would you like to generate one (H/G): ", color='yellow', inpt=True, fp=fp)
    if HaveKey.upper() == "H":
      PublicKey = sprint(txt="? Please enter public key:\n", color='yellow', inpt=True, fp=fp)
      PrivateKey = False
      try:
        rsa.encrypt("testtext".encode(), PublicKey)
      except:
        exit()
    elif HaveKey.upper() == "G":
      KeyLen = sprint(txt="? Do you want to specify a key length or use a random key length (S/R): ", color='yellow', inpt=True, fp=fp)
      if KeyLen.upper() == "S":
        keylen = sprint(txt="? Please enter key length (At least 16). Also keep in mind the key must be larger than the message you plan to encrypt:\n", color='yellow', inpt=True, fp=fp)
        try:
          keylen = int(keylen)
        except:
          exit()
      elif KeyLen.upper() == "R":
        keylen = random.randint(200,512)
      else:
        exit()
      PublicKey, PrivateKey = rsa.newkeys(keylen)
    else:
      exit()
    message = sprint(txt="? Input text to be encrypted:\n", color='yellow', inpt=True, fp=fp)
    try:
      encMessage = rsa.encrypt(message.encode('utf-8'), PublicKey)
    except:
      exit()
    sprint(txt=f"Public Key:\v{PublicKey}\n", color='green', fp=fp)
    if not PrivateKey:
      print("", end="")
    else:
      sprint(txt=f"Private Key:\v{PrivateKey}\n", color='green', fp=fp)
    sprint(txt=f"Encrypted Text:\v{encMessage}", color='green', fp=fp)

  elif eord.upper() == "D":
    Key = sprint(txt="? Please enter private key:\n", color='yellow', inpt=True, fp=fp)
    PKey = {
      "n": "",
      "e": "",
      "d": "",
      "p": "",
      "q": "",
    }
    for i in PKey:
      for i1 in Key:
        if i1 == ",":
          Key = Key[1:len(Key)+1]
          break
        elif i1 == " ":
          Key = Key[1:len(Key)+1]
          continue
        else:
          try:
            PKey[i] += str(int(i1))
            Key = Key[1:len(Key)+1]
          except:
            Key = Key[1:len(Key)+1]
            continue
    PrivateKey = rsa.PrivateKey(int(PKey["n"]), int(PKey["e"]), int(PKey["d"]), int(PKey["p"]), int(PKey["q"]))
    texttxt = str(sprint(txt="? Please input text to be decrypted:\n", color='yellow', inpt=True, fp=fp))
    texttxt = bytes(texttxt[2:len(texttxt)-1],'utf-8')
    print(texttxt)
    decMessage = rsa.decrypt(texttxt, PrivateKey).decode()
    sprint(txt=f"Private Key:\v{str(PrivateKey)}\n", color='green')
    sprint(txt=f"Decrypted Text:\v{str(decMessage)}", color='green', fp=fp)

else:
  exit()

sprint(txt="\n\nGoodbye!", color='green', fp=fp)
quit()