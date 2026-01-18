COMP 359, ON 1 Assignment 1 README

Our prompt was to use python nltk to download a list of words and have an AI model sort those words. We are looking to test current limitations of the AI's sorting abilities.

Some of the key statistics we are using to measure the AI's abilities are how many words the AI model can sort correctly, at what point does the AI start to have problems sorting and what kind of problems occur. As well we will be keeping track of how long it takes for the AI to sort different amounts of words.

Our plan to work through this assignment was to break the task into four different classes that work together to be both have the AI sort the list and track the statistics involved.

These four classes breakdown as such:
1) nltkWords.py
   This class creates a new local list of words using pythons nltk at any desired length we require for testing.
2) AiCall.py
   This is where we send this random list of pre generated words to our Gemini API with a prompt that has the model sort the list of words to the best of it's abilities. We also time how long this generation and sorting takes the AI to further analyze later.
3) sort_comparison.py
   Here we use python to generate a correctly sorted list and compare it against the AI's list and track when mistakes are made, what kind of mistakes were generated and how many mistakes there were.
4) Main.py
   This is the class that brings it all together. We have it send the AI multiple different lengths of lists and return us the above statistics gathered for easy comparison between various input lengths to clearly see what mistakes were made by the AI's sorting.

For the AI model we chose to use Gemini 3 API as it has a free version for developers that we could use to generate our sorted lists. The main problem was that we were maxing out the usage at high input values so we used multiple API keys at the same time to reduce the usage per key. *Note* to execute the code you must on run this line on your own python enviroment:
pip install google-genai

When running the list through our program we begin to see errors depending on how many words are attempted to be sorted. When about 400 words were included in the list the AI model would begin to fail and become very unreliable. Our largest value sorted with good accuracy was 320 words in which the AI correctly sorted 317 of those words and it took 2 minutes and 4 seconds for the words to be sorted. Lists below the 300 word mark were all correctly sorted without any mistakes. The time it took for those words to be sorted are shown in the graph below.
<img width="2520" height="1553" alt="ReliableDataGraphCOMP359" src="https://github.com/user-attachments/assets/cf60ad91-4d70-4327-b2b9-f4ec7772ba67" />
We saw the times for the sorting grew exponentially for this "reliable" data range which is when the amount of words was under 400.

The further we went beyond 400 words the less words would be sorted. Beginning at 640 words the AI model would struggle to sort 10 words correctly out of the whole list. The problems seen here are primarily missing and duplicated words. Often 90% of the words would be missing and the AI would repeat many of the same words instead of sorting the given list. One thing we noticed with the time it takes at these large input values is that it seems to be logarithmic in nature instead of expontential. Both these issues could be caused by the amount of tokens we are sending to the API is meeting or exceeding the maximum amounts granted to us by the free API we are using. Meaning that potentially the model gives up and stops generating early but nonetheless we thought to include these findings. The graph of these large input values is given below.
<img width="2892" height="1796" alt="LargeDataGraphCOMP359" src="https://github.com/user-attachments/assets/7659a346-8233-4f79-9ae5-60cb6443f23c" />

In this table below we show the number of words sorted along with the amount of words the AI model sorted correctly. This really shows how much the AI struggles when it comes to these larger inputs. But also how it can be useful and reliable for smaller lists of words.

Number of words sorted | Words sorted correctly 
           5                       5
           10                      10
           20                      20
           40                      40
           80                      80
           160                     160
           320                     317
           640                      3
           1280                     1
           2560                     29
           5120                     3
           10240                    4
           20480                    8
           40960                    2

Overall as seen in the graphs the time to sort the words within the 400 word range is manageable with list lengths of 50 taking under 10 seconds and ists of 320 words taking around 2 minutes and still sorting reliably. The longest possible list would be capped by the amount of tokens you are allowed to send to the AI model. But as we discovered there are large struggles with these large inputs not only with the time it takes but also the effectiveness of the sorting. These large values (2,000-40,000) take upwards of 7 minutes to sort and in most cases under 10 words were sorted correctly. Even though small problems were seen around 300 words the sorting was still reliable and the massive sorting errors of repeating and missing words were not present. 

Bibliography:

Amos, David, “Object-Oriented Programming (OOP) in Python”, Real Python, https://realpython.com/python3-object-oriented-programming/ 

Kumar, Pankaj and Walia, Anish, “Python Compare Strings - Methods & Best Practices”, Digital Ocean, 2025, https://www.digitalocean.com/community/tutorials/python-string-comparison

Obregon, Alexander, “Beginner’s Guide to Understanding Python Syntax”, Medium, 2024, https://medium.com/@AlexanderObregon/a-beginners-guide-to-understanding-python-syntax-649ccf10ce5e

“OpenAI Platform.” Tokenizer, platform.openai.com/tokenizer

“Using Gemini Api Keys | Google AI for Developers.” Gemini API, ai.google.dev/gemini-api/docs/api-key
