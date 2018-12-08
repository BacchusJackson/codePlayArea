import hashlib
import getpass

def inputToHash(inText = ""):
    if inText == "" :
        usrInput = raw_input('enter String: ' )
        byteMsg = bytes(usrInput)
    else:
        byteMsg = bytes(inText)

    mHash = hashlib.sha256()
    mHash.update(byteMsg)

    return mHash.hexdigest()

def login():
    password = getpass.getpass('Password: ')
    password = (password, "!") [password == ""]
    if inputToHash(password) == '9734661b68cf1fc5e1c50d8da2298a2b25dc1219b6437a1376eb29769fc15991':
        return True
    else:
        return False

num = 0
status = False

while True:
    status = login()
    num=num+1
    if num >= 3:
        print("Max number of attempts reached!")
        exit()
    if status == False:
        print("Login Fail. Please try again. Number of Attempts: " + str(num))
    else:
        break


print("Success!")

