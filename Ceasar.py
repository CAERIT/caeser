
def shift(data,key):
    phrase = ""
    while key < 0:
        key += 26
    while key >=26:
        key -= 26

    for char in data:
        if ord(char) ==32:
            phrase += char
            continue
        newchar = ord(char)+key
        if ord(char) <=90 and newchar >90:
            newchar -=26
        if ord(char) >96 and newchar > 122:
            newchar -=26
        phrase += chr(newchar)
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
        results = decryptLoop(message)
        for key in results:
            print(key,"(",26-key,"):",results[key])
    else:
        print("select e or d")

    


if __name__ == "__main__":
    main()
    
