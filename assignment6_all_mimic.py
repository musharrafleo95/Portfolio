"""Mimic pyquick exercise -- optional extra exercise.
Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next word.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(file_of_words):   #function to get all words 
    file_object = open(file_of_words,"r")  #creating a file object
    unique_element = []
    s = file_object.read() #reading the file object
    s = s.lower()    #converting to lowercase
    all_element = s.split() #splitting the words
    
    for element in all_element:
        if element not in unique_element:  # getting all the unique elements
            unique_element.append(element)
            
    new_dict = {} #creating a mimic dict
    
    for element in unique_element: #making all the keys of element which are unique in paragraph
        new_dict[element] = []
        
    for element in unique_element: #for each fundamental element in unique_element
        count = 0  #for index of the upcomming element
        
        for sub_element in all_element:  #so that we can see each element in the paragraph and compare each unique element of list unique_element with all the element of list all_element
            
            if sub_element == element: #if found one of the element of unique_element in all_element then appened the next element of it to its list which is in the dictionary
                
                if count == len(all_element) - 1: #if any of the element is last  then it will break and will not show out of range error 
                    break
                else:
                    new_dict[element].append(all_element[count + 1])
            
            count += 1
    return new_dict
  


def print_mimic(mimic_dict, word):
    list_of_keys = []
    
    for key in mimic_dict.keys(): #so that we can work for a case where a word is not present in mimic dictionary
        list_of_keys.append(key)
    count = 1   #counter for printing 200 words
    
    ############ function for error we get when we select random variable from an empty list ############################
    def no_empty_error(x):
        if x == []: #if no word in a list
            print("")
        else:
            x = random.choice(x) #else choose a random word
            print(x)
    ######################################################################################################################
    
    
        
    x = word #just storing it in a variable
    while(count < 201):
        if (x not in list_of_keys):  #if a word not in list of keys then print a random word from a dictionary"
        
            x = mimic_dict[random.choice(list_of_keys)]
            no_empty_error(x)
        else:                       #or just print random word from a dict
            x = mimic_dict[x] #now storing the list of that word which was print before
            no_empty_error(x)
            
        count += 1
    


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
