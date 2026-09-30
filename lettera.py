
word=input('Enter a word to see if it has the letter a in it')
for i in word:
    if i in "Aa":
        print("a has been found")
        break
    else:
        print("a is not found")