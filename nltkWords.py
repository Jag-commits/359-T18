#Make sure to pip install nltk into the venv
import nltk
import random

#Python doesn't enforce explicit return types, but it's good practice to type hint to avoid errors
def retrieveWords() -> list:
    #If the Words folder already exist, just use the words
    try:
        nltk.data.path.append("./Words")
        from nltk.corpus import words
        word_list = words.words()
        return word_list
    #If the Words folder doesn't exist, make it
    except:
        createWords()
        from nltk.corpus import words
        word_list = words.words()
        return word_list

def createWords():
    #Download the words into a local folder
    nltk.download('words', download_dir='./Words')
    #NLTK was looking in the wrong directories, need to actually append the directory
    nltk.data.path.append("./Words")
    print("Words Created")
    
#Just a function to repeatedly call based on the length of the desired list
def randomWordsList(length : int, wordlist: list[str]) -> list[str]: 
    #I doubt we'd actually reach this point, but edge case gets handled
    #I initially made a if, but this is so much cleaner
    length = min(length,len(wordlist))

    randomlist =random.sample(wordlist,length)
    #Super and super are etymologically the same, it's just that Super is capitalized. I don't see how Super > super just on the basis of capitalization if the words are exactly the same
    #Therefore, I'm making all the words lowercase to ensure the sorting algorithm won't define Super>super instead of Super = super
    for x in range(0,length):
        randomlist[x] = randomlist[x].lower()

    return randomlist



