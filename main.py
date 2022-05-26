# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if(len(word) != len(anagram)):
        return False
    return (sorted(word)==sorted(anagram))
    
word = input("Enter a word: ")
anagram = input("Enter another word:")

find_anagram(word,anagram)