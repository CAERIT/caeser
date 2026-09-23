
def shift(data,key):
    phrase = ""
    for char in data:
        phrase += chr(ord(char)+key)
    return phrase
        

def main():
    message = input("enter your message: ")
    key = int(input("enter your key: "))
    print("resulting output: ", shift(message,key))


if __name__ == "__main__":
    main()
    
