#Make sure to 'pip install google-genai' into your venv for this to work
from google import genai
import time
#I can't put the API Key on Github
GEMINI_API_KEY=""

#Python doesn't do explicit return types so I need to use type hinting
def GeminiCall(words = list) -> dict:
    #Using API Docs from Google, to interact with Gemini's free tier API: https://ai.google.dev/gemini-api/docs/api-key
    client = genai.Client(api_key=GEMINI_API_KEY)
    words = str(words)
    prompt = "This prompt does not require extensive thinking. Return only the sorted list, don't say hello, don't say here you go, do not say anything apart from the sorted list. The sorting method should not consider whether the word is capitalized or not, if it's uppercase make it lowercase. The list should be seperated by commas, there should not be any [] or any type of brackets/parenthesis/apostrophies/quotation marks. Here is the List:" + words
    timestart= time.perf_counter()
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        #AI's prompt goes here, will be dynamically adjusted with the array
        contents=prompt,
    )
    result = response.text
    timestop = time.perf_counter()

  

    #Create a list from the string of sorted words
    listWords=[]
    #edge cases where the model adds spaces at either end :/ 
    result = result.strip()
    for word in result.split(","):
        word = word.lower()
        #model can sometimes add spaces after each comma
        listWords.append(word.strip())
    return {
        "returnList" : listWords,
        "timeelapsed": (timestop-timestart)
            }

