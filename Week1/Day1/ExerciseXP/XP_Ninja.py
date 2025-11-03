# Exercise 1 : Use the terminal
print(r"""
Quand on installe Python pour la première fois, on voit en bas du manuel d'installation
une case à cocher : add python to path.
Et lors de l'exécution de la commande PATH dans le terminal, on distingue ces deux lignes :
C:\\Users\\Others\\AppData\\Local\\Programs\\Python\\Python314\\Scripts\\
C:\\Users\\Others\\AppData\\Local\\Programs\\Python\\Python314\\
Cela signifie que les dossiers où Python 3.14 est installé sur mon ordinateur,
Windows sait très bien où trouver Python sans que tu te déplaces dans le dossier lui-même.
Alors quand tu tapes python au terminal : Windows cherche ce programme dans chaque dossier du PATH
selon l'ordre, dès qu'il trouve le fichier python.exe il l'exécute.
""")


# Exercise 2 : Alias
print(r"""
Un alias est un raccourci ou un surnom pour une commande.
Qui permet d'exécuter une commande longue à l'aide d'un mot court.
Alors une fois on exécute la commande py dans le terminal, on obtient ce résultat : 
Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Cela signifie que vous avez ouvert le shell interactif Python et que vous pouvez désormais saisir directement du code Python.
""")

# Exercise 3 : Outputs
3 <= 3 < 9   #True
3 == 3 == 3  #True
bool(0)      #False
bool(5 == "5") #False
bool(4 == 4) == bool("4" == "4") #True
bool(bool(None))  #False
x = (1 == True)   
y = (1 == False)  
a = True + 4      
b = False + 10    

print("x is", x)  #x is True
print("y is", y)  #y is False
print("a:", a)    #a: 5
print("b:", b)    #b: 10


# Exercise 4 : How many characters in a sentence ?
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))

# Exercise 5: Longest word without a specific character
longest_sentence = ""
while True :
    longest_word=input("Write a sentence without an A : ")

    if 'A' in longest_word.upper():
        print("That has an 'A'! Try again.")
    elif len(longest_word) > len(longest_sentence):
        longest_sentence=longest_word
        print("Congrats! That's your longest sentence ")
    else :
        print("Not longer enough, try again!")
    



