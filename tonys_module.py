"""1) Has a function to calculate the square footage of a house
Reminder of Formula: Length X Width == Area"""

def area(length, width):
    area_result = length * width
    return area_result
print(area())

"""2) Has a function to calculate the circumference of a circle
Program in Jupyter Notebook should take in user input and use 
imported functions to calculate a circle's circumference or a houses square footage"""

def circumference(radius):
    result = (3.14 * radius) ** 2
    return result
print(circumference())

