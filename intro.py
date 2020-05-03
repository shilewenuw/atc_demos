x = 5
y = 'Jeff'
x = 'abc'  # you can change x from an int to a string no problem in Python because of dynamic typing.
# static typing is when you give a type to a variable, like int x = 5. Then x = "abc" would be illegal


# visualize indices (remember arrays start at 0)
#    0  1  2  3
a = [2, 2, 3, 4]  # this is a list
print(a[0])

# the following access the same element in our context
print(a[3])
print(a[len(a)-1])  # len() is a built in Python function to get length of an object
                        # we access last element intelligently (remember arrays start at 0, so 4 is out of bounds)
print(a[-1])  # Pythonic shorthand for above


# def means function, think of math functions, f(x) = x^2
# f(0) = 0, f(3) = 9, etc.
def square(x):
    return x*x

# you can store functions in variables
func = square

print(func(3))

# func2  = def square(x): return x*x <--- how to convert this into a legal one liner
func2 = lambda i: i*i

print(func2(3))

# add one to all items in list using list comprehension
y = [o+1 for o in a]
print(y)

# square all items in list using list comprehension
z = [func2(r) for r in a]

# class keyword denotes that we are creating a class
class Dog:
    def __init__(self, breed, weight):
        self.breed = breed
        self.weight = weight
    def bark(self):
        print('bark')
    def print_info(self):
        self.bark()
        print(self.breed)
        print(self.weight)

d1 = Dog('chonker', 500)
d1.print_info()

# example of class extension
class ViolentDog(Dog):
    def attack_the_drug_kingpin(self, name):
        print('attacked: ', name)
    def give_weight(self):
        print(self.weight)

d2 = ViolentDog('husky', 200)
d2.attack_the_drug_kingpin('Walter White')
# you can also use methods from class you extended/inherited from
d2.print_info()

# classes allow reusability of code
class GoodPupper(Dog):
    def wimper(self):
        print('*sad dog noises*')

d3 = GoodPupper('doge', 50)
d3.wimper()

x = [5, 2, 3, 4]

for a in x:
    print(a)

# Java equivalent for next for loop
# for (int x=0; i < 10; i++){
#     System.out.println(x)
# }

for x in range(10):
    print(x)

b = 0
while b < 10:
    print(b)
    b += 1

