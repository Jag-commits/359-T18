#Make sure to 'pip install google-genai' into your venv for this to work
from google import genai
import time
#I can't put the API Key on Github
key1=""
key2=""
global GEMINI_API_KEY
GEMINI_API_KEY=key1

#Python doesn't do explicit return types so I need to use type hinting
def GeminiCall(words = list) -> dict:
    attempt = 0
    global GEMINI_API_KEY
    #Using API Docs from Google, to interact with Gemini's free tier API: https://ai.google.dev/gemini-api/docs/api-key
    client = genai.Client(api_key=GEMINI_API_KEY)
    words = str(words)
    for attempt in range(2):
        try:
            prompt = "This prompt does not require extensive thinking. Return only the sorted list, don't say hello, don't say here you go, do not say anything apart from the sorted list. The sorting method should not consider whether the word is capitalized or not, if it's uppercase make it lowercase. The list should be seperated by commas, there should not be any [] or any type of brackets/parenthesis/apostrophies/quotation marks. Here is the List:" + words
            timestart= time.perf_counter()
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                #AI's prompt goes here, will be dynamically adjusted with the array
                contents=prompt,
            )
            result = response.text 
            

            #edge cases where the model adds spaces at either end :/ 
            result = result.strip()

            #Observed Gemini returning null or "", "/n" strings
            if not result:
                raise Exception("Empty response")
             
            timestop = time.perf_counter()
            #Request worked, no more attempts needed
            break
        except:
            #We don't want an infinite loop of failed attempts
            if attempt<1:
                print("\nError: Retrying\n")
                time.sleep(5)
                continue
            else:
                #We'll use this to skip this length
                return {"returnList" :"AI Model failed to respond after 2 attempts"}

  

    #Create a list from the string of sorted words
    listWords=[]
    
    for word in result.split(","):
        word = word.lower()
        #model can sometimes add spaces after each comma
        listWords.append(word.strip())

   #Cycle through API keys to get a total of 40 requests per day, and 10 per minute
    
    if GEMINI_API_KEY==key1:GEMINI_API_KEY=key2
    else:GEMINI_API_KEY=key1
    

    return {
        "returnList" : listWords,
        "timeelapsed": (timestop-timestart)
            }

