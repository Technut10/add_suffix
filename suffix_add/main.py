import re, sys

# User Input

singleWord = input("Enter a word: ")
singleWord = singleWord

# Suffixes

suf1 = 'ing'
suf2 = 'ly'


def errorCheck():

	# Makes sure only alphanumeric letters are used.

    if not re.match("^[a-z]*$", singleWord):
        print("Please enter letters")
        sys.exit()


def addEndOfWord():

    if len(singleWord) < 3:
        print(singleWord)

    elif singleWord.endswith(suf1):
        
        print(singleWord + suf2)


    elif singleWord != singleWord.endswith(suf1):
        print(singleWord + suf1)
    
    else: 
        pass
 

 
errorCheck()
addEndOfWord()


