# This file is fulfill the remaining requirements in this project.

# Inheritance req:


class drink:
    def __init__(self):
        self.name = ''

    def setName(self, n):
        self.name = n


class junk(drink):
    def __init__(self):
        super().__init__()
        self.why = ''

    def setWhy(self, s):
        self.why = s

# Recursion req


def countUpToTen(num):
    if (0 <= int(num) <= 10):
        if (num != 0):
            countUpToTen(num - 1)
            print(num, end=' ')
            return
        else:
            print(num, end=' ')
            return


# Dictionary req
dictionary = {"Doggy": 1, "Kitty": 2,
              "Parrot": 3, "Lizard": 4, "Fish": 5}


# Use the following to test everything above...
"""
# Enter a number up to 10
countUpToTen(10)
print()

for x, y in dictionary.items():
    print(x, y)

a = drink()
a.setName('Tea')
b = junk()
b.setName('Pepsi')
b.setWhy('Caffeine')

print("Drink A:", a.name)
print("Drink B:", b.name, "\t\tWhy: ", b.why)
"""
