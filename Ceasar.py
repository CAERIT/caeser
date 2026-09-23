
def shift(data,key):
    phrase = ""
    for char in data:
        phrase += chr(ord(char)+key)
    return phrase
        

def main():
    print(shift("hello",1))

if __name__ == "__main__":
    main()
    
