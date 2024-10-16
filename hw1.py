import math
import data
from data import (Price, Rectangle, Book, Circle, Point, Employee)
# Write your functions for each part in the space below.

# Part 1
def vowel_count(word:str) -> int:
    counter = 0
    start = 0
    vowels = "AaEeIiOoUu"
    while start < len(word):
        if word[start] in vowels:
            counter += 1
        start += 1
    return counter

# Part 2
def short_lists(nums:list[list[int]]) -> list[list[int]]:
    result = [[item[0], item[1]] for item in nums]
    return result

# Part 3
def ascending_pairs(nums:list[list[int]]) -> list[list[int]]:
    list_x = []
    for element in nums:
        if len(element) == 2 and element[0] > element[1]:
            list_x.append([element[1], element[0]])
        else:
            list_x.append(element)
    return list_x

# Part 4
def add_prices(num:Price,num2:Price) -> Price:
    dollars  = num.dollars + num2.dollars
    cents = num.cents + num2.cents
    while cents >= 100:
        dollars += cents // 100
        cents = cents % 100

    return Price(dollars, cents)

# Part 5
def rectangle_area(shape:Rectangle) -> int:
    width = (shape.bottom_right.x - shape.top_left.x)
    height = (shape.top_left.y - shape.bottom_right.y)
    result = round(abs(width * height))
    return result

# Part 6
def books_by_author(author:str, books:list[Book]) -> list[Book]:
    result = []
    for book in books:
        if author in book.authors:
            result.append(book)
    return result

# Part 7
def circle_bound(Rectangle) -> Circle:
    center_point = Point((Rectangle.top_left.x + Rectangle.bottom_right.x) / 2,(Rectangle.top_left.y + Rectangle.bottom_right.y) / 2)
    radius = 0.5 * math.sqrt((Rectangle.top_left.x - Rectangle.bottom_right.x) **2 + (Rectangle.top_left.y - Rectangle.bottom_right.y) **2)
    return Circle(center_point, radius)

# Part 8
def below_pay_average(workers:list[Employee]) -> list[str]:
    average_pay = sum(worker.pay_rate for worker in workers) / len(workers)
    below_average = [worker.name for worker in workers if worker.pay_rate < average_pay]
    return below_average

