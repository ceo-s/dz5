from math import sqrt, pi, pow, hypot
import pytest
import random


def test_sqrt():
    num = random.randint(1, 9999)
    assert round(sqrt(num)**2) == num

def test_pow():
    x, y = random.randint(1, 100), random.randint(1, 10)
    assert pow(x, y) == x**y


def test_hypot():
    x, y = random.randint(1, 15), random.randint(1, 10)
    assert hypot(x, y) == sqrt(sum([x**2, y**2]))

def test_sorted1():
    list = [6,4,7,3,2,8,9,1,5,0]
    assert sorted(list) == [0,1,2,3,4,5,6,7,8,9]

def test_sorted2():
    list = ["Anton", "Masha", "Zoya", "Aaron", "Sonya"]
    assert sorted(list) == ['Aaron', 'Anton', 'Masha', 'Sonya', 'Zoya']

def func_for_map(num: int=0):
    return str(num)

def test_func_for_map():
    x = random.randint(1,100)
    assert func_for_map(x) == str(x)

def test_map1():
    assert list(map(func_for_map, [1, 2, 3, 10, 999])) == ["1", "2", "3", "10", "999"]

def filter_func(x):
    return x if x[0] == "O" else False

def test_filter():
    assert list(filter(lambda x: x if x[0] == "O" else None, ["Origami", "Ferrum", "Ann", "Osho", "Cinnamon"])) == ['Origami', 'Osho']


test_filter()
print(list(filter(lambda x: x if x[0] == "O" else None, ["Origami", "Ferrum", "Ann", "Osho", "Cinnamon"]) ))
print(list(map(func_for_map, [1,2,3])))

print(sorted(["Anton", "Masha", "Zoya", "Aaron", "Sonya"]))
print(pi)
print(sqrt(2) + sqrt(3))