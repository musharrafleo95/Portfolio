"""Wordcount exercise
Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.


def intermediate_word(file_of_words):   #function to get all words and their count
    file_object = open(file_of_words,"r")  #creating a file object
    unique_element = []
    count_dict = {}
    s = file_object.read() #reading the file object
    s = s.lower()    #converting to lowercase
    x = s.split() #splitting the words
    
    for element in x:
        if element not in unique_element:  # getting all the unique elements
            unique_element.append(element)
    
    for element in unique_element:  # finding count of all elements
        element_appear = 0 #counter to count appearance of same strings
        
        for element_of_x in x: #checking unique element against each element of passed string
            if element_of_x == element: # if same element found then increase counter
                element_appear += 1
                
        count_dict[element] = element_appear #storing them in a dictionary
    
    return count_dict


def print_words(s):
    dict_of_items = intermediate_word(s)
    list_of_keys = []
    
    
    for key in dict_of_items.keys():
        list_of_keys.append(key)
    
    list_of_keys.sort()
    
    for key in list_of_keys:
        print(key + " : " + str(dict_of_items[key]))

def print_top(s):
    dict_of_items = intermediate_word(s)
    list_of_values = []
    for value in dict_of_items.values(): #getting all values from a dict
        list_of_values.append(value)
    list_of_values.sort(reverse = True) #to get values in descending order
    
   ############################################################################### 
    
    def remove_adjacent(nums):  #to avoid same values being print multiple times
        new_list = []
        if len(nums) == 0:
            return new_list
        else:
            new_list.append(nums[0]) # write this statement because it was giving out of index error
            for elements in nums:
                if elements != new_list[len(new_list)-1]:
                    new_list.append(elements)
            return new_list
        
    ################################################################################    
        
    
        
    list_of_values = remove_adjacent(list_of_values)   #using the above function
    count = 1 #so that only 20 top words can be print
    
    
    for value in list_of_values:  #taking one value from list of values so that we can compare it with each value in dictionary
        for key, value_dict in dict_of_items.items():
            if value_dict == value: # here each value of dict is being compared with the unique value of list
                if count < 21: # when count exceedes 20 then printing stop
                    print(key + " : " + str(dict_of_items[key]))
                    count += 1

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
