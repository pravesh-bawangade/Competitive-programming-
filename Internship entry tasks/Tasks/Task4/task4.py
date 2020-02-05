"""
File Name : task4.py
Author : Pravesh Bawangade
Functions: 1. vocabBuilder(path) - Building Vocabulary.
           2. vocabEncoding(sample, vocab) - Encoding string using vocabulary. 
"""
import pandas as pd
from random import shuffle
from random import seed

def vocabBuilder(path):
    """
    This function takes in path of text file and build vocab dictionary and returns the same.
    Inputs: path- path of text file from which vocab should be built.
    Returns: Vocab dictionary.
    """
    text = open(path,"r+", encoding="utf-8")  
    text = str(text.read()).split()
    
    #Calculating Frequency
    freq = dict()
    for word in text:
        freq[word] = text.count(word)

    #Checking for the words having frequency 1.
    ones = [i for i in freq.keys() if freq[i] == 1]
    
    #Removing random 40% of words having frequency 1.
    seed(1)
    data = [*range(round(len(ones)*0.4))]
    shuffle(data)
    ones = [ones[i] for i in data]
    for i in ones:
        del freq[i]
    
    # Creating Vocab dictionary
    data = [*range(1,len(freq.keys()))]
    keys = [*freq.keys()]
    shuffle(data)
    vocab = dict()
    for i in range(len(data)):
        vocab[keys[i]] = data[i]

    return vocab

def vocabEncoding(sample, vocab):
    """
    This function takes in sample string and vocab dictionary and encode it.
    Inputs: sample - sample string to encode.
            vocab - vocab dictionary
    returns: encoded list.
    """
    sample = sample.split()
    x = []
    for i in sample:
        try:
            x.append(vocab[i])
        except:
            x.append("NID")
    return x

if __name__ == "__main__":
    print("Building Vocabulary using test.txt file....")
    vocab = vocabBuilder("test.txt")
    print("Encoding string 'The black community’s long history of entrepreneurship'")
    sample = "The black community’s long history of entrepreneurship"
    list_en = vocabEncoding(sample, vocab)
    print("Encoded list")
    print(list_en)
    print("NID means Not In Dictionary - This word has freq 1 and may have removed while cleaning 40'%' of such words.")