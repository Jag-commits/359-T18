from AiCall import *
from nltkWords import *
from sort_comparison import *
import time

#Start by retrieving (Or creating and then retrieving) the list of total words
word_list = retrieveWords()

#The shuffled length starts from 5, and expands until it hits the max length
shuffledLength = 128 

#Account will run out of tokens if I put this too high
maxlength = 10240

#Repeat loop until we start seeing errors
noErrors = True

#Time to sort list -> Nice to know how time taken to sort grows with list length
Tts=[]

while noErrors:
    shuffledlist = randomWordsList(shuffledLength,word_list)
    #Stored in Dictionary
    AIResponse = GeminiCall(shuffledlist)
    #Extract Values from GeminiCall method
    AItime = AIResponse["timeelapsed"] #Time to sort
    AISortedList = AIResponse["returnList"] #Sorted List
    Tts.append(round(AItime,5))
    #Records the time elapsed for the model to return the sorted list
    print(f"Current List Length: {shuffledLength}")
    print(f"Time taken to sort: {AItime}")
    
    

    #Stored in Dictionary
    compareResults = compareSorted(shuffledlist,AISortedList)
    #End loop when first error found
    if compareResults["firstErrorLocation"] != None:
        noErrors=False

        #Store all issues with AI Sorted List
        correctlySorted = compareResults["correctlySorted"]
        missingWords = compareResults["missingWords"]
        extraWords = compareResults["extraWords"]

        #Display Which Errors Exist
        print()
        print(f"Error Found:\nLength of List: {shuffledLength}")
        if correctlySorted !=0 : print(f"Number of Correctly Sorted Words: {correctlySorted}")
        if missingWords !=0:print(f"Number of Missing Words: {missingWords}")
        if extraWords !=0:print(f"Number of Extra Words: {extraWords}")

        break

    print("All Good")
    shuffledLength= shuffledLength*2
    time.sleep(15) #Trying to Keep under Gemeni's 5 Requests per Minute
    if shuffledLength==maxlength:noErrors=False


   
    

    









