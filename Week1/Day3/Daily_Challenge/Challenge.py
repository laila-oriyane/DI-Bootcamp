# 1. Letter Index Dictionary
word = input('Enter a Word : ')
letter_index={}
for index,letter in enumerate(word) :
    if letter in letter_index :
        letter_index[letter].append(index)
    else :
        letter_index[letter]=[index]
print(letter_index)
    
# 2. Affordable Items
# 1. Store Data:
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"
# 2. Data Cleaning:
clean_wallet = int(wallet.replace("$","").replace(",",""))

basket = []
# 3. Determining Affordable Items:
for item,price in items_purchase.items() :
    clean_price = int(price.replace("$","").replace(",",""))
    if clean_wallet >= clean_price :
        basket.append(item)
        clean_wallet -= clean_price   

if len(basket) > 0 :
    print(sorted(basket))
else :
    print("Nothing")
