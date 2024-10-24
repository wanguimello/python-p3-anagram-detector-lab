# your code goes here!

# lib/anagram.py

class Anagram:
    def __init__(self, word):
        # Store the word as lowercase and sorted letters for easy comparison
        self.word = word.lower()
    
    def match(self, words):
        # This will store any anagram matches
        matches = []
        
        # Sort the original word once to avoid sorting multiple times
        sorted_word = sorted(self.word)
        
        # Iterate over each word in the list of potential anagrams
        for word in words:
            # Compare the sorted letters of each word
            if sorted(word.lower()) == sorted_word:
                matches.append(word)
        
        # Return the list of matches (empty if no matches found)
        return matches
