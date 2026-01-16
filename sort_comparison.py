def compareSorted(original: list[str], ai_sorted: list[str]) -> dict:
#Create the correctly sorted list
    correct = sorted(original)

#Initialize tracking variables to compare the lists
    correctlySortedWords = 0         #Tracks number of correctly sorted words
    missingWords = 0            #Tracks number of missing unique words
    extraWords = 0              #Tracks number of extra unique words
    duplicateWords = 0          #Tracks number of duplicate words
    firstErrorLocation = None   #Tracks the location of the first error made by the AI sorted list

#Find which list is shorter and make that the furthest point for comparison
    limit = min(len(correct), len(ai_sorted))

#Compare the known sorted list to the AI models sorted list
    for i in range(limit):
        if correct[i] == ai_sorted[i]:      #Increment correctly sorted counter if words match
            correctlySortedWords += 1

        else:
            if firstErrorLocation is None:  #Record the first point words do not match
                firstErrorLocation = i

#Create hash sets to compare the lists
    correct_set = set(correct)
    ai_set = set(ai_sorted)

#Find the amount of words that are missing in the AIs list
    missingWords = len(correct_set - ai_set)

#Find how many words are only in the AIs list (Mainly duplicates)
    extraWords = len(ai_set - correct_set)

#Count duplicate words produced by the AI model
    from collections import Counter
    correct_counts = Counter(correct)
    ai_counts = Counter(ai_sorted)

#Any extra words in the AI list not in the expected list are duplicates
    for word, count in ai_counts.items():
        allowed = correct_counts.get(word, 0)
        if count > allowed:
            duplicateWords += count - allowed

#If the list lengths are different and no errors are found in the comparison then the first error is the first word after the correctly sorted list
    if len(ai_sorted) != len(correct) and firstErrorLocation is None:
        firstErrorLocation = limit

#Return the comparison results
    return {
        "inputSize": len(original),
        "correctlySortedWords": correctlySortedWords,
        "missingWords": missingWords,
        "extraWords": extraWords,
        "duplicateWords": duplicateWords,
        "firstErrorLocation": firstErrorLocation
    }
