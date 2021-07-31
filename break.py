print (""" 
Hello you must enter the secret 
word the first 4 letters are chup
""")

word = ["chupacabra"]
counter = 0 


while True:
    guess = input ("enter your word ")
    if guess == word:
        print ("Your correct the word is", word)
        break
    counter += 1
    if counter != 0:
        print("This word", guess,"is not correct" )
else:
    print("You haven't entered any guesses.")
    