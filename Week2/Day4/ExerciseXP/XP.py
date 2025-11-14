# Exercise 1: Random Sentence Generator
import random 
import json

def get_words_from_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        words = content.split()
        return words

def get_random_sentence(length):
    words = get_words_from_file("words.txt")
    sentence_words = []
    if not words:
        return "No words available to generate a sentence."

    for _ in range(length):
        random_word = random.choice(words)
        sentence_words.append(random_word)

    sentence = " ".join(sentence_words).lower()
    return sentence

def main():
    print(" Welcome to the Random Sentence Generator!")
    print("This program generates a random sentence of your chosen length (between 2 and 20).")

    try:
        length = int(input("Enter sentence length (2–20): "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if length < 2 or length > 20:
        print("Error: Length must be between 2 and 20.")
        return

    sentence = get_random_sentence(length)
    print("\n Your random sentence:")
    print(sentence)

# Run program
main()

# Exercise 2: Working with JSON
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Step 1: Load the JSON string
data = json.loads(sampleJson)
# Step 2: Access the nested “salary” key
salary = data["company"]["employee"]["payable"]["salary"]
print("Salary",salary)
# Step 3: Add the “birth_date” key
data["company"]["employee"]["birth_date"] = "1999-05-12"
# Step 4 : Save JSON to a file
with open("modified.json", "w") as file:
    json.dump(data, file, indent=4)