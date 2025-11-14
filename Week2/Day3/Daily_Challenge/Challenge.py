import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    # 1. Compute area
    def area(self):
        return math.pi * (self.radius ** 2)
    
    # 2. Print attributes
    def __str__(self):
        return f"Circle(radius={self.radius})"
    
    # 3. Add two circles → return new circle
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        return NotImplemented
    
    # 4. Compare which circle is bigger
    def __gt__(self, other):
        return self.radius > other.radius
    
    # 5. Check if two circles are equal
    def __eq__(self, other):
        return self.radius == other.radius
    
    # 6. Sorting circles → define "less than"
    def __lt__(self, other):
        return self.radius < other.radius
        
c1 = Circle(5)
c2 = Circle(3)
c3 = Circle(5)

print(c1.area())                  # Aire
print(c1)                         # Affichage

c4 = c1 + c2                      # Addition
print(c4)

print(c1 > c2)                    # True
print(c1 == c3)                   # True

circles = [c1, c2, c3, Circle(1)]
sorted_circles = sorted(circles)

for c in sorted_circles:
    print(c)
