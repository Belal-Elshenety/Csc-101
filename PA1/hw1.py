import data
import math

def vowel_count(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

def short_lists(nested_lists:list[list[int]])->list[list[int]]:
    return [lst for lst in nested_lists if len(lst)==2]

def ascending_pairs(lists):
        result = []
        for lst in lists:
            if len(lst) == 2:
                result.append(sorted(lst))
            else:
                result.append(lst)
        return result

def add_prices(p1:list[data.Price], p2:list[data.Price]):
    dollars = p1.dollars + p2.dollars
    cents = p1.cents + p2.cents
    if cents >= 100:
        dollars += cents // 100
        cents = cents % 100
    return [dollars,cents]

def rectangle_area(d:list[data.Rectangle]):
    return d.top_left * d.bottom_right

def books_by_author(author_name:str, books:list[data.Book])-> str:
    return [book for book in books if book.authors == author_name]

def circle_bound(rectangle:list[data.Rectangle]):
    center = data.Point((rectangle.top_left.x + rectangle.bottom_right.x)/2, (rectangle.top_left.y + rectangle.bottom_right.y)/2)
    diameter = math.sqrt((rectangle.top_left.x - rectangle.bottom_right.x)**2 + (rectangle.top_left.y - rectangle.bottom_right.y)**2)
    radius = diameter / 2
    return data.Circle(center, radius)

def below_pay_average(employee_list:list[data.Employee])->list[str]:
    if not employee_list:
        return []
    total_pay = sum([employee.pay_rate for employee in employee_list])
    average_pay = total_pay / len(employee_list)
    below_average = [employee.name for employee in employee_list if employee.pay_rate < average_pay]
    return below_average
