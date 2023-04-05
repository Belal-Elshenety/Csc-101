import unittest
import hw1
import data

class Testhw1(unittest.TestCase):
    def test_val_count1(self):
        input = "Hello World"
        result = hw1.vowel_count(input)
        expected = 3
        self.assertEqual(expected,result)

    def test_val_count2(self):
        input = "Computer science"
        result = hw1.vowel_count(input)
        expected = 6
        self.assertEqual(expected,result)

    def test_short_lists1(self):
        input = [[1,2],[2,3,4],[5,6,7],[5,6]]
        result = hw1.short_lists(input)
        expected = [[1,2],[5,6]]
        self.assertEqual(expected,result)

    def test_short_lists2(self):
        input = [[1,2],[2,3,4],[5,6,7],[5,6],[7,9],[2,3],[6,5]]
        result = hw1.short_lists(input)
        expected = [[1,2],[5,6],[7,9],[2,3],[6,5]]
        self.assertEqual(expected,result)

    def test_ascending_pairs1(self):
        input = [[3,2],[5,6,7],[5,3],[4,9,2]]
        result = hw1.ascending_pairs(input)
        expected = [[2,3],[5,6,7],[3,5],[4,9,2]]
        self.assertEqual(expected,result)

    def test_ascending_pairs2(self):
        input = [[3,2],[5,6,7],[5,3],[4,9,2],[8,7,9],[4,2],[6,3]]
        result = hw1.ascending_pairs(input)
        expected = [[2,3],[5,6,7],[3,5],[4,9,2],[8,7,9],[2,4],[3,6]]
        self.assertEqual(expected,result)

    def test_add_prices1(self):
        input1 = data.Price(1,78)
        input2 = data.Price(2,57)
        result = hw1.add_prices(input1,input2)
        expected = [4,35]
        self.assertEqual(expected,result)

    def test_add_prices2(self):
        input1 = data.Price(3,63)
        input2 = data.Price(2,91)
        result = hw1.add_prices(input1,input2)
        expected = [6,54]
        self.assertEqual(expected,result)

    def test_rectangle_area1(self):
        input = data.Rectangle(7,2)
        result = hw1.rectangle_area(input)
        expected = 14
        self.assertEqual(expected,result)

    def test_rectangle_area2(self):
        input = data.Rectangle(9,6)
        result = hw1.rectangle_area(input)
        expected = 54
        self.assertEqual(expected,result)
    def test_books_by_author1(self):
        book1 = data.Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        book2 = data.Book(["Robert Kiyosaki"], "Rich dad poor dad")
        book3 = data.Book(["Robert Kiyosaki"], "Another book")
        input1 = ["Robert Kiyosaki"]
        input2 = [book1 , book2, book3]
        result = hw1.books_by_author(input1,input2)
        expected = [data.Book(["Robert Kiyosaki"], "Rich dad poor dad"),data.Book(["Robert Kiyosaki"], "Another book")]
        self.assertEqual(expected, result)

    def test_books_by_author2(self):
        input = [data.Book(["Rick Riordan"], "Percy Jackson: The Lightning Thief"), data.Book(
            ["Rick Riordan"], "Percy Jackson: The Sea of Monsters"), data.Book(["Rick Riordan"], "The Lost Hero"),data.Book(["Robert Kiyosaki"], "Rich dad poor dad")]
        expected = [data.Book(["Rick Riordan"], "Percy Jackson: The Lightning Thief"), data.Book(
            ["Rick Riordan"], "Percy Jackson: The Sea of Monsters"), data.Book(["Rick Riordan"], "The Lost Hero")]
        result = hw1.books_by_author(["Rick Riordan"],input)
        self.assertEqual(expected, result)

    def test_circle_bound1(self):
        result = data.Circle(data.Point(3.0, 3.0), 5.0)
        rect = data.Rectangle(data.Point(0, -1), data.Point(6, 7))
        self.assertEqual(result, hw1.circle_bound(rect))

    def test_circle_bound2(self):
        result = data.Circle(data.Point(3.5, 3.0), 2.5)
        rect = data.Rectangle(data.Point(2, 1), data.Point(5, 5))
        self.assertEqual(result, hw1.circle_bound(rect))

    def test_below_pay_average1(self):
        result = ["Charles", "Ben", "Huey"]
        employees = [data.Employee("Charles", 15), data.Employee("Benjamin", 20), data.Employee(
            "Tom", 25), data.Employee("Ben", 16), data.Employee("Joey", 23), data.Employee("Huey", 16)]
        self.assertEqual(result, hw1.below_pay_average(employees))

    def test_below_pay_average2(self):
        result = ["Belal", "Sam", "Anthony"]
        employees = [data.Employee("Belal", 20), data.Employee("Sam", 22), data.Employee(
            "Anthony", 23), data.Employee("Ben", 30), data.Employee("Joey", 28), data.Employee("Huey", 29)]
        self.assertEqual(result, hw1.below_pay_average(employees))