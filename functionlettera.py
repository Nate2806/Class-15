def letterA(word):
    for i in (word):
       if i in "Aa":
        print("A, is in the word")
        break
       else:
        print("A, is not found in this word") 
word=input("Enter a word to find if it has A in it: ")
letterA(word)
