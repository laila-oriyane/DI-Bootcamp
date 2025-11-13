import math
# Step 1: Create the Pagination Class
class Pagination :
# Step 2: Implement the __init__ Method
    def __init__(self,items,page_size=10):
        if items is None:
            self.items=[]
        self.items=items #items we have in the list
        self.page_size=page_size #The number of items you want per page
        self.current_idx=0  #start at first page
        self.total_pages=math.ceil(len(self.items) / self.page_size)  #Divides total items by the number per page
        #calculates how many pages are needed to show all items, even if the last page is not completely full

# Step 3: Implement the get_visible_items() Method
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

# Step 4: Implement Navigation Methods

   # Goes to the specified page numbe
    def go_to_page(self,page_num):
        index = page_num - 1 #pages are stored internally starting at 0
        if index in range(self.total_pages): #index exist
            self.current_idx=index
        else:
            raise ValueError("Page number Invalid !")
        return self

   # Navigates to the first page
    def first_page(self):
        self.current_idx=0
        return self
   # Navigates to the last page.
    def last_page(self):
        self.current_idx=self.total_pages - 1
        return self
   # Moves one page forward (if not already on the last page)
    def next_page(self):
        if self.current_idx < self.total_pages - 1 :
            self.current_idx += 1
        return self
   # Moves one page backward (if not already on the first page)
    def previous_page(self):
        if self.current_idx > 0 :
            self.current_idx -= 1
        return self

# Bonus :
# Step 5: Add a Custom __str__() Method
    def __str__(self):
    # gets all items that should appear on the current page
        visible_items = self.get_visible_items()
    # join them into a string, each item on a new line
    # Join all strings with a newline, so each item prints on its own line
        return "\n".join(str(item) for item in visible_items)


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']
print(str(p))

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']
print(str(p))

p.last_page()
print(p.get_visible_items())
# ['y', 'z']
print(str(p))

p.go_to_page(3)
print(p.get_visible_items())
# ['i', 'j', 'k', 'l']
print(str(p))

# p.go_to_page(10)
# print(p.current_idx + 1)
# Output: ValueError

# p.go_to_page(0)
# Raises ValueError
# Bonus
print(p.next_page().next_page().next_page().get_visible_items())
print(str(p))
