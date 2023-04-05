# list_tests.py
import unittest
import list


# Write your test cases for each part below each instructor test


class TestCases(unittest.TestCase):
    def test_init(self):
        testing = list.List(5)
        result = [None, None, None, None, None]
        self.assertEqual(result, testing.list)

    def test_init2(self):
        testing = list.List(2)
        result = [None, None]
        self.assertEqual(result, testing.list)


    def test_add(self):
        testing = list.List(3)
        testing.add(0)
        testing.add(1)
        testing.add(2)
        result = [0, 1, 2]
        self.assertEqual(result, testing.list)

    def test_add2(self):
        testing = list.List(3)
        testing.add(4)
        testing.add(7)
        testing.add(9)
        result = [4,7,9]
        self.assertEqual(result, testing.list)

    def test_remove(self):
        testing = list.List(3)
        testing.add(0)
        testing.add(1)
        testing.add(2)
        testing.remove(0)
        result = [1, 2]
        self.assertEqual(result, testing.print_list())

    def test_remove2(self):
        testing = list.List(3)
        testing.add(4)
        testing.add(6)
        testing.add(7)
        testing.remove(0)
        result = [6,7]
        self.assertEqual(result, testing.print_list())

    def test_get_length(self):
        testing = list.List(7)
        self.assertEqual(7, testing.get_length())

    def test_get_length2(self):
        testing = list.List(3)
        self.assertEqual(3, testing.get_length())

    def test_get_num_items(self):
        testing = list.List(5)
        testing.add(0)
        testing.add(1)
        testing.add(2)
        testing.remove(0)
        self.assertEqual(2, testing.get_num_items())

    def test_get_num_items2(self):
        testing = list.List(5)
        testing.add(3)
        testing.add(7)
        testing.add(1)
        testing.remove(1)
        self.assertEqual(2, testing.get_num_items())

    def test_insert(self):
        testing = list.List(6)
        testing.add(0)
        testing.add(2)
        testing.add(2)
        testing.add(3)
        testing.add(4)
        testing.remove(1)
        testing.insert(1, 1)
        result = [0, 1, 2, 3, 4]
        self.assertEqual(result, testing.print_list())

    def test_insert2(self):
        testing = list.List(9)
        testing.add(2)
        testing.add(1)
        testing.add(8)
        testing.add(4)
        testing.remove(1)
        testing.insert(1, 1)
        result = [2,1,8,4]
        self.assertEqual(result, testing.print_list())

    def test_second_dimension_ec(self):
        testing = list.List(5)
        testing.add(0)
        testing.add(4)
        testing.add(5)
        test = [1, 2, 3]
        result = [[0, 0, 0], [4, 8, 12], [5, 10, 15]]
        self.assertEqual(result, testing.second_dimension_ec(test))

    def test_second_dimension_ec2(self):
        testing = list.List(5)
        testing.add(2)
        testing.add(3)
        testing.add(6)
        test = [3,4,5]
        result = [[6,8,10], [9,12,15], [18,24,30]]
        self.assertEqual(result, testing.second_dimension_ec(test))


if __name__ == '__main__':
    unittest.main()
