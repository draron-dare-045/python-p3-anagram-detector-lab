# lib/anagram.py
class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, possible_anagrams):
        # Sort the characters of the word and check for matches in the list
        sorted_word = sorted(self.word)
        return [anagram for anagram in possible_anagrams if sorted(anagram) == sorted_word]
