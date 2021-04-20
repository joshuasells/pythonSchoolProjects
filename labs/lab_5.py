# Joshua Sells, Intro to computer science, 10/06/2019, lab_5.py, this program display the number of time a word is used.

def main():
    
    #get a phrase of english words. Remove the punctuation, lowercase every character, and split the words up into a list.
    engWords = removePunc(input('Enter English words: ')).lower().split()
    
    #display each word used in the phrase and how often it has been used.
    displayWordCount(engWords)
    

#loop through every character to see if it is punctuation and create a new list leaving the punctuation behind.   
def removePunc(engWords):
    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    engWordsNoPunc = ''

    for ch in engWords:
        if ch not in punctuations:
            engWordsNoPunc += ch
    return engWordsNoPunc

#assign every word as a key in a dictionary and increment its value for every time it is used. Then print the results.
def displayWordCount(engWords):
    print(format('Word', '20'), 'Count')
    print('-------------------------')
    
    wordCount = {}
    
    for word in engWords:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    for key, value in wordCount.items():
        print(format(key, '20'), value)
    
main()
    