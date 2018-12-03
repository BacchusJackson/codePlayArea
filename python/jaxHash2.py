msg = input('message: ')

alphabet='abcdefghijklmnopqrstuvwxyz'
key = 5
encMsg = ''

for i in msg:
    position=alphabet.find(i)
    newPosition=position+5%26

    encMsg +=alphabet[newPosition]
print(encMsg)
