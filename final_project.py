# -*- coding: utf-8 -*-
"""
Created on Thu May  1 18:34:13 2017

@author: impca
"""

from lxml import html
import requests
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from operator import itemgetter
from collections import defaultdict
from collections import Counter

def index_words(link):
    # getting html content of web pages
    page = requests.get(link)
    tree = html.fromstring(page.text)
    #creates a list of contents on webpage:
    raw_docs = tree.xpath('//p[@class="story-body-text story-content"]/text()')
    unique = set()

    # removing stop words, converting into lower case and removing non-english words
    for item in raw_docs:
        lower= re.sub('[^a-z]',' ',item.lower())
        striped = lower.strip()
        word_list = str(striped).split(" ")
        flatten = [word for word in word_list if (word not in stopwords.words('english') and word)]
        for word in flatten:
            unique.add(word)
#emulating a trei 
    # mapping words to web url
    
    for word in unique:
        if word in engine: # append the new word to the existing array at this slot
            engine[word].append(link)
        else:
            # create a new array 
            engine[word] = [link]

# reading the input file with list of urls
def read_list(path):
    text=open(path)
    fin = text.read()
    links=fin.split('\n')
    return links

if __name__ == "__main__":
    
    engine = defaultdict(list) # special container dictionary
    #rank = Counter(list)#special dictionary of words with word_count as key
    #enginer = sorted(rank.items(),key=itemgetter(0), reverse = True)# we get (word,count) by .items and sorted, sorts in desc 
    links = read_list('web.txt')
    for link in filter(None,links):
        index_words(link)

    # search

    k = input("search:")
    if k in engine:
        print(engine[k])

        

    '''for k,v in engine.items():
        print ("{},{}".format(k,v))'''
