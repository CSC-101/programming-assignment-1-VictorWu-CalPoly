import data
from data import (Price, Rectangle, Point, Book, Circle, Employee)
import hw1
import unittest

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        word = ("Apple")
        result = hw1.vowel_count(word)
        expected = 2
        self.assertEqual(expected, result)

    def test_vowel_count_2(self):
        word = ("Skibidi")
        result = hw1.vowel_count(word)
        expected = 3
        self.assertEqual(expected, result)

    # Part 2
    def test_short_lists_1(self):
        x = [[2,3,4,5,6], [2,5,76,7,2], [2,7,14,8,2,4,7]]
        result = hw1.short_lists(x)
        expected =[[2,3], [2,5], [2,7]]
        self.assertEqual(expected, result)

    def test_short_lists_2(self):
        x = [[78,50,4,5], [76,7,2], [14,8,7]]
        result = hw1.short_lists(x)
        expected =[[78,50], [76,7], [14,8]]
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending_pairs_1(self):
        x = [[2,3], [1], [8,5], [11,10]]
        result = hw1.ascending_pairs(x)
        expected = [[2,3], [1], [5, 8], [10,11]]
        self.assertEqual(expected, result)

    def test_ascending_pairs_2(self):
        x = [[2,3,5,7], [3,1], [50,8], [10, 11, 12]]
        result = hw1.ascending_pairs(x)
        expected = [[2,3,5,7], [1,3], [8,50], [10,11,12]]
        self.assertEqual(expected, result)

    # Part 4
    def test_add_prices_1(self):
        result = hw1.add_prices(Price(9,28), Price(10,99))
        expected = Price(20,27)
        self.assertEqual(expected, result)

    def test_add_prices_2(self):
        result = hw1.add_prices(Price(11,30), Price(35,80))
        expected = Price(47,10)
        self.assertEqual(expected, result)

    # Part 5
    def test_rectangle_area_1(self):
        top_left = Point(1,4)
        bottom_right = Point(2,6)
        result = hw1.rectangle_area(Rectangle(top_left,bottom_right))
        expected = 2
        self.assertEqual(expected, result)

    def test_rectangle_area_2(self):
        top_left = Point(10,12)
        bottom_right = Point(2,7)
        result = hw1.rectangle_area(Rectangle(top_left,bottom_right))
        expected = 40
        self.assertEqual(expected, result)

    # Part 6
    def test_books_by_author_1(self):
        author = "Orwell"
        book1 = Book(["Orwell", "Eric Arthur Blair"], "Animal Farm")
        book2 = Book(["Shelley", "Wollstonecraft"], "Frankenstein")
        books = [book1, book2]
        result = hw1.books_by_author(author, books)
        expected = [book1]
        self.assertEqual(expected, result)

    def test_books_by_author_2(self):
        author = "Stroker"
        book1 = Book(["Stroker", "Bill"], "Dracula")
        book2 = Book(["Twain"], "Huckleberry")
        books = [book1, book2]
        result = hw1.books_by_author(author, books)
        expected = [book1]
        self.assertEqual(expected, result)

    # Part 7
    def test_circle_bound_1(self):
        top_left = Point(1,8)
        bottom_right = Point(7,4)
        result = hw1.circle_bound(Rectangle(top_left, bottom_right))
        expected = Circle(Point(4,6), 3.605551275463989)
        self.assertEqual(result.center, expected.center)
        self.assertAlmostEqual(result.radius, expected.radius)

    def test_circle_bound_2(self):
        top_left = Point(50,70)
        bottom_right = Point(100,50)
        result = hw1.circle_bound(Rectangle(top_left, bottom_right))
        expected = Circle(Point(75,60), 26.92582404)
        self.assertEqual(result.center, expected.center)
        self.assertAlmostEqual(result.radius, expected.radius)

    # Part 8
    def test_below_pay_average_1(self):
        w1= Employee("Alana", 30)
        w2= Employee("Brick", 40)
        w3= Employee("Concrete", 60)
        w4= Employee ("Grass", 100)
        workers = [w1, w2, w3, w4]
        result = hw1.below_pay_average(workers)
        expected = [w1.name, w2.name]
        self.assertEqual(expected, result)

    def test_below_pay_average_1(self):
        w1= Employee("POly", 0)
        w2= Employee("Cat", 0)
        w3= Employee("Dog", 0)
        w4= Employee ("Blue", 0)
        workers = [w1, w2, w3, w4]
        result = hw1.below_pay_average(workers)
        expected = []
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
