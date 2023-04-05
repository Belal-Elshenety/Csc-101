import unittest
import data
import hw2

class Testhw2(unittest.TestCase):
    def test_create_rectangle1(self):
        input1 = data.Point(2,2)
        input2 = data.Point(10,10)
        result = hw2.create_rectangle(input1,input2)
        expected = data.Rectangle(data.Point(2,10),data.Point(10,2))
        self.assertEqual(expected,result)

    def test_create_rectangle2(self):
        input1 = data.Point(6,9)
        input2 = data.Point(7,2)
        result = hw2.create_rectangle(input1,input2)
        expected = data.Rectangle(data.Point(6,9),data.Point(7,2))
        self.assertNotEqual(expected,result)

    def test_shorter_duration_than1(self):
        input1 = data.Duration(4,12)
        input2 = data.Duration(3,39)
        result = hw2.shorter_duration_than(input1,input2)
        expected = True
        self.assertNotEqual(expected,result)

    def test_shorter_duration_than2(self):
        input1 = data.Duration(5,39)
        input2 = data.Duration(6,51)
        result = hw2.shorter_duration_than(input1,input2)
        expected = True
        self.assertEqual(expected,result)

    def test_song_shorter_than1(self):
        input1 = [data.Song("Artist1","Title1",data.Duration(1,31)),
                  data.Song("Artist2","Title2",data.Duration(3,51)),
                  data.Song("Artist3","Title3",data.Duration(7,32))]
        input2 = data.Duration(3,59)
        result = hw2.song_shorter_than(input1,input2)
        expected = [data.Song("Artist1","Title1",data.Duration(1,31)),
                  data.Song("Artist2","Title2",data.Duration(3,51))]
        self.assertEqual(expected,result)

    def test_song_shorter_than2(self):
        input1 = [data.Song("Artist1","Title1",data.Duration(1,31)),
                  data.Song("Artist2","Title2",data.Duration(3,51)),
                  data.Song("Artist3","Title3",data.Duration(7,32))]
        input2 = data.Duration(3,59)
        result = hw2.song_shorter_than(input1,input2)
        expected = [data.Song("Artist1","Title1",data.Duration(1,31))]
        self.assertNotEqual(expected,result)

    def test_running_time1(self):
        input1 = [data.Song("Artist1", "Title1", data.Duration(4, 30)),
                  data.Song("Artist2", "Title2", data.Duration(3, 40)),
                  data.Song("Artist3", "Title3", data.Duration(3, 29)),
                  data.Song("Artist4", "Title4", data.Duration(3, 58))]
        input2 = [0, 2, 1, 3, 0]
        result = hw2.running_time(input1,input2)
        expected = data.Duration(20,7)
        self.assertEqual(expected, result)

    def test_running_time2(self):
        input1 = [data.Song("Artist1", "Title1", data.Duration(2, 11)),
                  data.Song("Artist2", "Title2", data.Duration(3, 12)),
                  data.Song("Artist3", "Title3", data.Duration(1, 37)),
                  data.Song("Artist4", "Title4", data.Duration(3, 29))]
        input2 = [0, 2, 1, 3, 0]
        result = hw2.running_time(input1, input2)
        expected = data.Duration(12, 40)
        self.assertEqual(expected, result)
    def test_validate_route1(self):
        city_links = [['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = ['san luis obispo', 'santa margarita', 'atascadero']
        expected = True
        result = hw2.validate_route(city_links,route)
        self.assertEqual(expected,result)

    def test_validate_route2(self):
        city_links = [['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = ['san luis obispo', 'atascadero']
        expected = True
        result = hw2.validate_route(city_links,route)
        self.assertNotEqual(expected,result)

    def test_longest_repetition1(self):
        list = [1, 1, 2, 2, 1, 1, 1, 3]
        expected = 4
        result = hw2.longest_repetition(list)
        self.assertEqual(expected,result)

    def test_longest_repitition2(self):
        list = [3,3,5,5,4,4,7,7]
        expected = 0
        result = hw2.longest_repetition(list)
        self.assertEqual(expected, result)