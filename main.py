from AiCall import *
from nltkWords import *
from sort_comparison import *
import time

#Start by retrieving (Or creating and then retrieving) the list of total words
word_list = retrieveWords()

#The shuffled length starts from 5, and expands until it hits the max length
shuffledLength = 5

#Account will run out of tokens if I put this too high
maxlength = 10240

#Repeat loop until reached max
notMax = True

#Time to sort list -> Nice to know how time taken to sort grows with list length
Tts=[]

#Lengths with Errors
Lwe=[]

#Lengths With No Errors
Lwne=[]

while notMax:
    shuffledlist = randomWordsList(shuffledLength,word_list)
    #Stored in Dictionary
    AIResponse = GeminiCall(shuffledlist)
    #Extract Values from GeminiCall method
    AItime = AIResponse["timeelapsed"] #Time to sort
    AISortedList = AIResponse["returnList"] #Sorted List
    #The model failed after 2 attempts and thus we're skipping it
    if AISortedList=="AI Model failed to respond after 2 attempts": 
        print(AISortedList)
        continue
    Tts.append((shuffledLength,round(AItime,5)))
    #Records the time elapsed for the model to return the sorted list
    print(f"Current List Length: {shuffledLength}")
    print(f"Time taken to sort: {AItime}")
    
    

    #Stored in Dictionary
    compareResults = compareSorted(shuffledlist,AISortedList)
    #Loop to describe Error until longest possible (Limited by API Free-Tier) input
    if compareResults["firstErrorLocation"] != None:
        Lwe.append(shuffledLength)

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
    else:
        print("All Good")
        Lwne.append(shuffledLength)
    shuffledLength= shuffledLength*2
    time.sleep(15) #Trying to Keep under Gemeni's 5 Requests per Minute
    if shuffledLength>maxlength:notMax=False
if len(Lwe)!=0:print(f"Lengths with Errors: {Lwe}\nFirst Error At Length: {Lwe[0]}")
print(f"Lengths with no Issues: {Lwne}")
print(f"Time Growth for Sorts (Length,Time): {Tts}")



   
    

    









