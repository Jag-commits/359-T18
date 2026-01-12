def compareSorted(original: list[str], ai_sorted: list[str]) -> dict:
    #Create the correctly sorted list
    correct = sorted(original)

    #Initialize tracking variables to compare the lists
    correctlySorted = 0     #Tracks number of correctly sorted words
    missingWords = 0        #Tracks number of missing words
    extraWords = 0         #Tracks number of extra words
    firstErrorLocation = None       #Tracks the location of the first error made by the Ai sorted list

    #Determine the limit for comparison based on the shorter list incase the Ai sorted list is missing or has extra words
    limit = min(len(correct), len(ai_sorted))

    #Compare the correctly sorted list to the Ai models sorted list
    for i in range(limit):
        #increment correctly sorted count if the Ai sorted word matches the correct word
        if correct[i] == ai_sorted[i]:
            correctlySorted += 1
        #If the Ai's word does not match, check if it's the first error and record its location
        else:
            if firstErrorLocation is None:
                firstErrorLocation = i

    #Check if the the Ai's list is missing words
    if len(ai_sorted) < len(correct):
        missingWords = len(correct) - len(ai_sorted)
        if firstErrorLocation is None:
            firstErrorLocation = limit

    #Check if the the Ai's list has extra words
    elif len(ai_sorted) > len(correct):
        extraWords = len(ai_sorted) - len(correct)
        if firstErrorLocation is None:
            firstErrorLocation = limit

    return {
        "inputSize": len(original),
        "correctlySorted": correctlySorted,
        "missingWords": missingWords,
        "extraWords": extraWords,
        "firstErrorLocation": firstErrorLocation
    }
