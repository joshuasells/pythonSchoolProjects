# Joshua Sells, Intro to computer science, 09/29/2019, lab_4.py, this program is a simple scrable game.

def display_banner():
    print("""
 __                               _      _            _ 
/ _\  ___  _ __  __ _  _ __ ___  | |__  | |  ___   __| |
\ \  / __|| '__|/ _` || '_ ` _ \ | '_ \ | | / _ \ / _` |
_\ \| (__ | |  | (_| || | | | | || |_) || ||  __/| (_| |
\__/ \___||_|   \__,_||_| |_| |_||_.__/ |_| \___| \__,_|
                                                        
""")

def load_words(filename):
    #load file containing scrambled word and answer.
    #scrambled word and answer are sparated by :

    scrambled_list = []
    answer_list = []
    with open(filename, 'r') as f:
        for line in f:
            (s,a) = line.strip().split(":")
            scrambled_list+=[s]
            answer_list+=[a]
    return (scrambled_list, answer_list)
            
            
def main():
    
    display_banner()
    import random

    
    (scrambled_list, answer_list) = load_words('halloween.txt')
    
    #--------------------------
    
    keep_going = True
    
    # Randomly pick a scrambled word from the list.
    
    while keep_going == True:
        random_scrambled_word = random.choice(scrambled_list)
        scrambled_word_answer = answer_list[scrambled_list.index(random_scrambled_word)]
        print('Scrambled word is:', random_scrambled_word)

    # Asks the user to guess it.
    
        user_guess = input('What is the word? ')
    
    # Ask again if the guess is wrong.  Rpeat until the guess is right.
    
        while user_guess != scrambled_word_answer:
            print('Wrong answer. Try again!')
            print('Scrambled word is:', random_scrambled_word)
            user_guess = input('What is the word? ')
    # If guess is right, ask if user wants another game.
        print('You got it!')
        another = input('Another game? (Y/N): ')
        
        while another != 'Y' and another != 'y' and another != 'N' and another != 'n':
            another = input('Please enter (Y/N): ')
        if another == 'N' or another == 'n':
            print('Bye!')
            keep_going = False
    #--------------------------

        
main()

            
                        
