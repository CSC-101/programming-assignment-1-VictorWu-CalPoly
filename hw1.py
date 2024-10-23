import math
from token import AMPER

import data
from data import (Price, Rectangle, Book, Circle, Point, Employee)
# Write your functions for each part in the space below.

# Part 1
def vowel_count(word:str) -> int:
    counter = 0                     #Counter for vowels in a string
    idx = 0                         #Index for string in list representation
    vowels = "AaEeIiOoUu"           #Vowel place
    while idx < len(word):          #While index < length of word:
        if word[idx] in vowels:     #Go through the word's letters/ indexes and if in vowels:
            counter += 1            #+1 to vowel counter
        idx +=  1                   #LOOP until idx > length of word in which it has completed going through each letter in the word for a vowel
    return counter

# Part 2
def short_lists(nums:list[list[int]]) -> list[list[int]]:
    result = [[item[0], item[1]] for item in nums]      #Grab the first and second index of each item in the list
    return result                                       #So in a nested list, this is grabbing the first 2 values for each list in the [list of lists].

# Part 3
def ascending_pairs(nums:list[list[int]]) -> list[list[int]]:
    list_x = []                                                 #Placeholder
    for element in nums:                                        #For each coordinate in the list of list (sublist) of integers:
        if len(element) == 2 and element[0] > element[1]:       #If there are 2 elements and the first element is > the second element:
            list_x.append([element[1], element[0]])             #Add both those elements reversed to the placeholder list
        else:
            list_x.append(element)                              #Else just add the element as is bc it doesn't meet conditions
    return list_x

# Part 4
def add_prices(num:Price,num2:Price) -> Price:
    dollars  = num.dollars + num2.dollars              #Dollars = adding the dollars tag from each given input
    cents = num.cents + num2.cents                     #Cents = adding the cents tag from each given input
    while cents >= 100:                                #While cents >= 100:
        dollars += cents // 100                         #Current Dollars + cents converted to dollars EX: Cents = 130 // 100 = 1 (int no remainder) .3 goes away
        cents = cents % 100                             #Current Cents + the remainder EX: Cents = 130 % 100 = 3
    return Price(dollars, cents)

# Part 5
def rectangle_area(shape:Rectangle) -> int:
    width = (shape.bottom_right.x - shape.top_left.x)       #Width = given coord
    height = (shape.top_left.y - shape.bottom_right.y)      #height = given coord
    result = round(abs(width * height))                     #Result = Abs value and rounded Width * Height
    return result

# Part 6
def books_by_author(author:str, books:list[Book]) -> list[Book]:
    result = []                             #Placeholder
    for book in books:                      #For every item/book in the list of Book objects:
        if author in book.authors:              #If the particular author is traced to the item/book's author:
            result.append(book)                     #Add book to the placeholder
    return result

# Part 7
def circle_bound(Rectangle) -> Circle:
    center_point = Point((Rectangle.top_left.x + Rectangle.bottom_right.x) / 2,(Rectangle.top_left.y + Rectangle.bottom_right.y) / 2)           #Center point formula: (x1 + x2)/2 + (y1 + y2)/2
    radius = 0.5 * math.sqrt((Rectangle.top_left.x - Rectangle.bottom_right.x) **2 + (Rectangle.top_left.y - Rectangle.bottom_right.y) **2)     #Radius: 1/2 * sqrt[(x1-x2)^2 + (y1-y2)^2]
    return Circle(center_point, radius)

# Part 8
def below_pay_average(workers:list[Employee]) -> list[str]:
    average_pay = sum(worker.pay_rate for worker in workers) / len(workers)                     #Average pay(int) = sum of worker.pay_rate (given) for each worker(item) in workers(list of Employees/ items)/ # of workers(items)
    below_average = [worker.name for worker in workers if worker.pay_rate < average_pay]        #Below Average(str) = Grabs worker's name for each worker(item) in list of Employees IF: worker.pay_rate(given) < average pay
    return below_average

