import sys
import string
import random
import re

e = 5 # used in encryption process
d = 37 # used in encryption process
N = 94 # Length of alphaNumKey, used in the encryption process
alphaNumKey = ['5', '*', 'M', 'i', '8', 't', '}', 'v', 'x', 'Y', '.', 'V', 'K', 'd', 'z', 'a', '|', '3', 'E', 'h', 'U', 'Q', ']', 'X', 'B', 'w', '<', 'k', 'Z', 'c', 'y', "'", 'J', 'b', '@', '\\', '+', 'P', 'R', 'l', 'm', '0', '=', 'A', ')', '[', 'F', '^', 'O', 'q', ':', '6', '"', '$', 'T', ',', 'N', '~', 'W', '%', '!', 'r', '>', 'L', '1', 'G', '7', 'I', 'p', '9', 'C', 'n', '`', 'S', '_', 'f', '-', 'H', 'g', '(', '{', 'e', '&', 'D', '4', 'o', '#', '2', 's', ';', '/', '?', 'j', 'u']
passKey = []
PWFileName = "PWMAN.txt"


def MakePrintable():
    tempStr = string.ascii_letters
    tempStr = tempStr + string.digits
    tempStr = tempStr + string.punctuation
    tempList = list(tempStr)
    random.shuffle(tempList)
    print(tempList)


def ENCDups():
    count = 0
    for x in range(95):
        cipher = ENCTest(x)
        message = DNCTest(cipher)
        print(x, cipher, message)
        if cipher == message:
            print("DUPLICATES")
            count += 1
    return count


def TestENC():
    message = "hello"
    print("Message: ", message)
    cipher = ENC(message)
    print("Cipher: ", cipher)
    message = DNC(cipher)
    print("DNC Message: ", message)
    return


def ENCTest(num):
    return (num**e) % N


def DNCTest(num):
    return (num**d) % N


def ENC(message):
    Cipher = ""
    for x in range(len(message)):
        if not message[x].isspace():
            Cipher = Cipher + (alphaNumKey[ENCTest(alphaNumKey.index(message[x]))])
        else:
            Cipher = Cipher + message[x]
    return Cipher


def DNC(cipher):
    message = ""
    for x in range(len(cipher)):
        if not cipher[x].isspace():
            message = message + (alphaNumKey[DNCTest(alphaNumKey.index(cipher[x]))])
        else:
            message = message + cipher[x]
    return message


def CreatePass():
    passWD = ""
    for x in range(12):
        passWD = passWD + random.choice(alphaNumKey)
    return passWD


if __name__ == '__main__':
    # todo ask user for GET or SET
    choice = input("GET password or SET password: ")
    choice = choice.upper()


    # todo if GET ask user for website name
    if choice == "GET":
        websiteName = input("What website do you need the password for? ")
        websiteName = websiteName.lower()
        # todo ask user for private key to decode PWMAN
        PrivateKey = input("What is your Private Key? ")
        # todo search doc for website, if there give website and password, otherwise say sorry and exit
        try:
            PWFile = open(PWFileName, "r")
        except IOError:
            print("ERROR: File does not appear to exist")
            empty = input("")
            exit(-1)
        Lines = PWFile.readlines()
        for line in Lines:
            line = DNC(line)
            if line.find(websiteName) > -1:
                print(line)
                empty = input("")
                exit(0)
        print("Website Not Found, please run again and use SET")
        empty = input("")
        exit(-1)

    # todo if SET ask user for website, username
    elif choice == "SET":
        # todo ask for public key to encode into PWMAN and validate key format
        while True:
            PublicKey = input("What is your Public Key? ")
            # Key = re.findall("\d+", PublicKey)
            Key = re.search("\d+,\s?\d+", PublicKey)
            if Key is None:
                print("Public Key in wrong format, try again")
            else:
                PublicKey = re.findall("\d+", PublicKey)
                break
        # print(PublicKey)

        # todo ask for website, username
        websiteName = input("What is the website name? ")
        websiteName = websiteName.lower()
        userName = input("What is your username for the website? ")
        PWD = CreatePass()
        setVar = str({websiteName: [userName, PWD]})
        # print(setVar)
        # todo open doc and encode given variables
        EncVar = ENC(setVar)
        try:
            PWFile = open(PWFileName, "r+")
        except IOError:
            print("ERROR: File does not appear to exist")
            empty = input("")
            exit(-1)
        content = PWFile.read()
        PWFile.seek(0, 0)
        PWFile.write(EncVar + '\n' + content)
        # todo close doc and exit
        PWFile.close()
        print("New Password is: ", PWD)
        empty = input("")

    exit(0)

