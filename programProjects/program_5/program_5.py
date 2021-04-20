# Joshua Sells, Intro to computer science, 10/15/2019, program_5.py, this program translates english words to hmong words.

def main():
    
    #load the dictionary file into a dictionary object to use with translating.
    dictionary = loadDictionary('dictionary.txt')    
    
    translateAgain = True
    wordCount = {}
    
    while translateAgain == True:
        #removes punctuation, lowercases, and splits the english sentence. A list named engWords is populated by the english sentence the user typed.
        engWords = removePunc(input('Type your english sentence: ')).lower().split()
        
        #keeps track of the words used.
        countWordFrequency(engWords, wordCount)
        
        #Translates the sentence and prints it.
        translate(engWords, dictionary)
    
        #prompt to repeat or not and validate the users input.
        again = input('Another translation (Y/N) : ')
    
        while again != 'Y' and again != 'y' and again != 'N' and again != 'n':
            again = input('Please enter a valid answer (Y/N) : ')
    
        if again.lower() == 'y':
            translateAgain = True
        else:
            translateAgain = False
    
    printWordFrequency(wordCount)

#Populates a dictionary with the contents of a file.    
def loadDictionary(filename):
    dictionary = {}
    with open(filename, 'r') as dictFile:
        for line in dictFile:
            (num, val, key) = line.split(',')
            dictionary[key.rstrip()] = val
    return dictionary

#Keeps track of the words used.   
def countWordFrequency(sentence, wordCount):
    for word in sentence:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    return wordCount

#loop through every character to see if it is punctuation and create a new list leaving the punctuation behind.   
def removePunc(sentence):
    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    engWordsNoPunc = ''

    for ch in sentence:
        if ch not in punctuations:
            engWordsNoPunc += ch
    return engWordsNoPunc

#translate the english words to hmong words and print them.
def translate(sentence, dictionary):
    print('Hmong: ', end='')
    for i in sentence:
        try:
            print(dictionary[i], end=' ')
        except KeyError:
            print('?', end=' ')
    print()
    
#print the total number of uses of each english word.   
def printWordFrequency(wordCount):
    print(format('Word', '20'), 'Frequency')
    print('------------------------------')
    for key, value in wordCount.items():
        print(format(key, '20'), value)
        
main()