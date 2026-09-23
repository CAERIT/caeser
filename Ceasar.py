
def shift(data,key):
    phrase = ""
    while key < 0:
        key += 26
    while key >=26:
        key -=26
    for char in data:
        phrase += chr(ord(char)+key)
    return phrase

def decryptLoop(data):
    outputDict=dict()
    for i in range(26):
        outputDict[i]=shift(data,i)
    return outputDict

def main():
    message = input("enter your message: ")
    choice = input("(e)ncrpyting or (d)ecrypting?:")
    if choice =="e":
        key = int(input("enter your key: "))
        print("resulting output: ", shift(message,key))
    elif choice =="d":
        print(decryptLoop(message))
    else:
        print("select e or d")

    


if __name__ == "__main__":
    main()
    
