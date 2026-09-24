import nltk
#download word list
#nltk.download("words", download_dir="./nltk_data")
from nltk.corpus import words
english_words = set(words.words())

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

def calcRatio(phrase):
    found = 0
    strcount = len(phrase.split(" "))
    for strword in phrase.split(" "):
        if strword in english_words:
            found +=1
    return found/strcount
        
    

def main():
    message = input("enter your message: ")
    choice = input("(e)ncrpyting or (d)ecrypting?:")
    if choice =="e":
        key = int(input("enter your key: "))
        print("resulting output: ", shift(message,key))
    elif choice =="d":
        results = decryptLoop(message)
        lable=0
        radic=dict()
        for key in results:
            radic[lable]=calcRatio(results[key])
            print(key,"("+str(26-key)+"):",results[key],radic[lable])
            lable+=1
        print("....................................")
        print("most likely result:",results[max(radic,key=radic.get)])


    else:
        print("select e or d")

if __name__ == "__main__":
    main()
    
