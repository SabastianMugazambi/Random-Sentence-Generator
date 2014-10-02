#Random sentence generator by Michael Vue and Sabastian Mugazambi
import sys
import random

def main():
    """obtains the file the user wants to generate random sentences from"""
    user_file = raw_input("Please enter a filename:")
    randomSentenceLoop(user_file)

def randomSentenceLoop(user_file):
    """ An infnite loop that gives the user the the option to generate another sentence or quit."""
    while True:
        option = raw_input("Press <Enter> to generate a random sentence; type 'quit' to quit. ")
        if option == 'quit':
            print "See you later!!"
            sys.exit()
        elif option == "":
            getUserFile(user_file)
        else:
            print "Sorry, I don't understand."

def getUserFile(user_file):
    """Gets the file the user calls and opens it and reads its contents then returns the contents."""
    book = (open(user_file,'r'))
    read_file = (book.read())
    wordList(read_file)
    book.close()
    return read_file

def  wordList(read_file):
    """Creates the word list from the contents of the file."""
    splitted = []
    temp = read_file.split()
    for word in temp:
        splitted.append(word.strip('\xef\xbb\xbf'))
    trainMarkovChain(splitted)
    return splitted

def trainMarkovChain(splitted):
      """Creates dictionary from the list of words obtained from the content of the file, then returns the dictionary."""
      dictionary = {}
      num_range = len(splitted)
      # i is the number relating to the index of the ith word from the list 'splitted'.
      # We subtract 1 to exclude the last word.
      for i in range(num_range-1):
          if dictionary.has_key(splitted[i]):
              dictionary[splitted[i]].append(splitted[i+1])
          else:
              dictionary[splitted[i]] = [splitted[i+1]]

      makeRandomSentence(dictionary)
      return dictionary

def getStartWord(dictionary):
        """ Finds words starting with capital letters and adds them to a list which will be used to randomly generate the starting word."""
        #creating a list of the keys in the dictionary and removing empty strings.
    	start = []
    	for key in dictionary.keys():
    			start.append(key)
        start = filter(None, start)
        #using the list to get starting words.
        start_word = []
        for word in start:
            if word[0].isupper():
                start_word.append(word)

        return start_word

def isEndWord(word):
    """ Loop that determines if a word is an end word and produces a boolean value to end the infinite loop or continue making the sentence."""
    if word.endswith('?') or word.endswith('.') or word.endswith('!'):
       x = True
    else:
       x = False
    return x




def makeRandomSentence(dictionary):
    """This is the function which continuosly produces words to edd to the random sentence until we get an end word."""
    sentence_list = []

#generating a random starting word.
    start_words_list = getStartWord(dictionary)
    starting_words_range = len(start_words_list)

    starting_word_index = random.randrange(0,starting_words_range,1)
    starting_word = start_words_list[starting_word_index]
    sentence_list.append(starting_word)


#generating random words given the random starting word.
    x = dictionary[starting_word]
    num_range = len(x)
    word_index = random.randrange(0,num_range,1)
    word = x[word_index]
    sentence_list.append(word)

#The infinite loop that generates a random word given the previous one.
    while True:
       if isEndWord(word) == False:
            word2_list = dictionary[word]
            num_range = len(word2_list)

            if num_range == 0:
                num_range = num_range + 1
            word_index = random.randrange(0,num_range,1)

            if word_index == 0:
                word = word2_list[word_index]
            else:
                word = word2_list[word_index-1]
            sentence_list.append(word)
       else:
            break

    print ' '.join(sentence_list)

main()