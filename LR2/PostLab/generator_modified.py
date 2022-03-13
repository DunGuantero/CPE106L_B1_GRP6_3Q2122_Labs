"""
Author: Gilroy Sio
Program: generator_modified.py
"""

import random

articles = lines = tuple([i.strip() for i in open("articles.txt", 'r').readlines()])
nouns = tuple([i.strip() for i in open("nouns.txt", 'r').readlines()])
verbs = tuple([i.strip() for i in open("verbs.txt", 'r').readlines()])
prepositions = tuple([i.strip() for i in open("prepositions.txt", 'r').readlines()])

def sentence():
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    number = int(input("Enter the number of sentences: "))
    for _ in range(number):
        print(sentence())

if __name__ == "__main__":
    main()

