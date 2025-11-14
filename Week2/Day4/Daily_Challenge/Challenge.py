import string
import re

class Text:
    # Step 1 : Constructor (__init__)
    def __init__(self, text):
        self.text = text
    
    def __str__(self):
        return self.text

    # Step 2 : word_frequency method
    def word_frequency(self, word):
        words = self.text.split()

        count = words.count(word)

        if count == 0:
            return None
        return count

    # Step 3 : most_common_word method
    def most_common_word(self):
        words = self.text.split()
        freq = {}

        for w in words:
            if w not in freq:
                freq[w] = 1
            else:
                freq[w] += 1

        # Find the word with the highest count
        most_common = max(freq, key=freq.get)
        return most_common

    # Step 4 : unique_words method
    def unique_words(self):
        words = self.text.split()
        unique_set = set(words)
        return list(unique_set)

    # Part II — Step 5 : from_file class method
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as file:
            content = file.read()
        return cls(content)
    
    # Bonus
class TextModification(Text):
    # Step 7 : remove_punctuation
    def remove_punctuation(self):
        punct = string.punctuation
        result = ""
        for char in self.text:
            if char not in punct:
                result += char
        return result

    # Step 8 : remove_stop_words
    def remove_stop_words(self):
        stop_words = [
    "a", "an", "the", "and", "or", "but", "if", "while", "is", "am", "are",
    "was", "were", "be", "been", "being", "do", "does", "did", "have", "has",
    "had", "in", "on", "at", "to", "from", "for", "of", "with", "as", "by",
    "about", "into", "over", "after", "before", "between", "during", "this",
    "that", "these", "those", "it", "its", "he", "she", "they", "them",
    "his", "her", "their", "you", "your", "we", "our", "me", "my", "mine",
    "yourself", "ourselves", "themselves", "i" 
    ]


        words = self.text.split()
        filtered_words = [w for w in words if w.lower() not in stop_words]
        return " ".join(filtered_words)

    # Step 9 : remove_special_characters
    def remove_special_characters(self):
        cleaned_text = re.sub(r"[^A-Za-z0-9\s]", "", self.text)
        return cleaned_text

txt = TextModification("Hello, word!!! This is a test $@$")
print("Original Text : ",txt)

print("Remove punctuation : ",txt.remove_punctuation())         
# Hello This is a test 

print("Remove stop words : ",txt.remove_stop_words())          
# Hello!!! This test $$$

print("Remove special characters : ",txt.remove_special_characters())  
# Hello This is a test 
