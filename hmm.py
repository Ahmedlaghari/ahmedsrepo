def encryption(text):
    temptext=""
    if len((text)) > 3:
        for i in range (len(text)):
          i=i+1
          temptext=temptext+text[-i]
        text =f"Iji{temptext}uop"
        return(text)
    else:
        for i in range (len(text)):
          i=i+1
          temptext=temptext+text[-i]
        text=temptext
        return (text)

def decryption(text):
  temptext=""
  if len((text)) > 3:
    lent = len(text)-6
    for i in range (lent):
      i=i+4
      temptext=temptext+text[-i]
    text = temptext
    return (text)
  else:
    for i in range(len(text)):
      temptext =temptext+text[-i]
    text = temptext
    return(text)
passw=input("enterpassword")      
print(encryption(passw))
