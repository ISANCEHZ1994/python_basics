# Given the below class:
class Cat:
    species = 'mammal'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 1 Instantiate the Cat object with 3 cats
Jerry = Cat('Jerry', 12)
George = Cat('George', 4)
Harry = Cat('Ernie', 23)

# 2 Create a function that finds the oldest cat
def oldest(*cats):
    oldest = {}
    age = 0
    for cat in cats:
        if cat.age > age:
            age = cat.age
            oldest.update({"name": cat.name, "age": cat.age})
    return oldest

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
cat = oldest(Jerry, George, Harry)

print(f'The oldest cat {cat["name"]} is {cat["age"]} years old.')
