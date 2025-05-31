# Python Lectures

## Lambda Functions

These are like functions without a name; they can have any number of arguments but only one expression. These are used as short operations or as arguments for higher-order functions.

```python
# Syntax
lambda arguments: expression
```

as a comparison, a basic function is:

```python
def addition(a,b):
    return a+b
```

If you have one expression, even with multiple parameters, you can create an anonymous or unnamed function, called a lambda function, with the same expression:

```python
addition = lambda a,b: a+b
```

This creates a function called addition, with a variable name, instead of using the functional definition statement. You can use it the same way with `addition(5,6)`.

Here's another example function:

```python
def even(num):
    if num%2 == 0:
        return True
```

You can convert this into a lambda function with:

```python
even1 = lambda num: num%2 == 0

# usage
even1(12)
```

You can write **any** number of parameters in the lambda function definition.

another example:

```python
addition1 = lambda x,y,z: x+y+z
```

The lambda function has great usages, especially when combined with the map and filter functions.

## Map Function Primer

If you want to perform a function on a list, like squaring every number, you might define a function that accepts a list like:

```python
def sqaure(number):
    return number**2
```

But for this we'd have to write a for loop to process this over a list. Instead of doing this as a for loop, you can use a _map_ function to apply this function to the entire list.

First we'd use a lambda function:

```python
numbers = [...] # list of integers

list(map( lambda x: x**2, numbers))
```

This setup returns the list of squared numbers. This is because the map function accepts, as its first parameter, a function, and as its second parameter, an iterable object. This performs the function on each value of the iterable object, but requires the `list()` function around it to capture those outputs into another list.

## Map Function Continued

The map function applies a function to every item in an input iterable and returns a map object. This is useful for transforming data in a list comprehensively.

If you have a list of numbers:

```python
numbers = [1,2,3,4,5,...]

def square(num):
    return num * num

# option 1: creating a for loop, appending to another list, etc.

# option 2, and better: you can directly use the map
# takes an input function, and an iterable as its input
map(square, numbers) # this takes every number and applies the function to each value, but creates a map object

list(map(square, numbers)) # this gives you back a list
```

### Lambda Functions with maps

You can use the map function with a lambda or unnamed function too:

```python
list(map(lambda x: x**x, numbers)) # same as option 2
```

You can then add an expression to anything using a lambda expression.

You can even use a map with multiple iterables:

```python
nums1 = [1,2,3]
nums2 = [4,5,6]

added_numbers = list(map(lambda x,y: x+y, nums1, nums2)) # adds these elements pair-wise to reutnr [5,7,9] by pulling x from the first list and y from the second list
```

You can use some of the default functions that are inbuilt within map too, like casting functions like `int`, or `str`, or literally **_ANY_** pre-defined function.

```python
words = [ ...]
capitalized_words = list(map(str.upper, words)) # capitalizes each word in words
```

You can use maps on a dictionary of items too.

for instance, if you want to use a dictionary function on each item of a dictionary:

```python
people = {...}

list(map(people['name'], people)) # grabs the `name` attribute for every item in the people dictionary.
```

## Filter Function

This constructs an iterable from elements of an iterable for a function whichs returns true; it is used to filter out items from a list based on a condition:

for instance, if you want to check if numbers are even:

```python
lst = [1,2,3,4,...]

# to get only the even integers from this, we can use filter instead of the module operator
# first parameter is a function, second parameter is a list
filter(lambda x: x%2 ==0, lst)
```

This is the basic use of filters, applying this to filter out data from the original iterable.

You can use this for any conditional statement, like greater than or equal to, or any other advanced expression with a lambda function.

You can use filter operations with multiple conditions too with the lambda functions:

```python
lst # from above

even_and_greater_than_five = list(filter(lambda x: x>5 and x%2==0, lst)) # see how we can use logical operators to extend the logic, but still creates an expression that evaluates as True or false
```

You can use this on any iterable, including dictionaries:

```python
people = {
    {'name':..., 'age':...}
}

age_greater_than_25 = list(filter(people['age'] > 25, people))
```

This is some of the great logic you can do with these functions.

You can use map and filter to efficiently process collections of data in Python.

---

# Magic Methods

These are double underscore methods which start and end with underscores, these enable you to define the behavior of an object for built in behaviors, like what happens when the object is cast into another type.

some examples of these are:

```python
__init__
__str__
__getitem__
__setitem__
# etc.
```

These define the behavior of the object for built-in operations. You can use this technique to overwrite the standard methods for an object:

```python
class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

person=Person("Aaron",35)
```

So effectively, when you start to write a new class, some of these methods are magic methods.

These are very important functionalities which are helpful for overwriting the basics of an object.

---

# Operator Overloading

We talked through magic methods, but there are some of these methods that define how to compare an object to other objects.

You could even overwrite how the addition operator works for a particular object. This is called `operator overloading`; these operators are defined as a set of magic functions:

```python
__add__
__sub__
__gt__ (greater than)
__eq__
__truediv__
__lt__
#etc.
```

for defining one of these you would do something like:

```python
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y


# these operator overloading enables you to write out vector operators as needed

def __add__(self,other):
    return Vector(self.x + other.x, self.y + other.y) # this lines up properties from the first object (self) and the second object (other)

def _sub__(self, other):
    return Vector(self.x - other.x, self.y - other.y)

# you can do these for all these functions and should do these for all these functions to enable all the mathematical operators to work appropriately
```

This is how you can overload your operators based on your assumptions or requirements.

You can overload this addition for complex numbers, which have an imaginary part; which is a good practice exercise.


