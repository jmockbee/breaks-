print (""" 
Hello you must enter the secret 
word the first 4 letters are chup
""")

word = ["chupacabra"]
counter = 0 


while True:
    guess = input ("enter your word ")
    if guess == word:
        break
    counter += 1
    if guess != word:
        
    