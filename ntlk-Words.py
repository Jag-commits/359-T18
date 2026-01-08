#Make sure to pip install nltk into the venv
import nltk


#Python doesn't enforce explicit return types, but it's good practice to type hint to avoid errors
def retrieveWords() -> list:
    #If the Words folder already exist, just use the words
    try:
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
    