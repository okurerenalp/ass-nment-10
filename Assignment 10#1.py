import pyAesCrypt

def encrypt(filename,password):
    pyAesCrypt.encryptFile(filename, (filename + ".enc"), password)

def decryp(filename,password):
    f = filename[:-4]
    pyAesCrypt.decryptFile(filename, f, password)

command  = input("Press 'e' to encrypt and 'd' for decrypt: ")
filename = input("Enter the file name: ")
password = input("Enter the password: ")

isDone = False

if(command == "e"):
    encrypt(filename,password)
elif(command == "d"):
    decryp(filename,password)
else:
    print(command + "is not a valid command.")