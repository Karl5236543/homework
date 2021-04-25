import pytest
import unittest
from homework3 import divisor_of_one_hundred, cached, not_str


#-------------------------------------------------------------------#
# doctest
#-------------------------------------------------------------------#
def sum1(a, b):
    """
    >>> sum1(10, 10)
    20
    >>> sum1(10, 20)
    30
    """
    return a + b


#-------------------------------------------------------------------#
# unittest
#-------------------------------------------------------------------#
class TestCached(unittest.TestCase):
    def setUp(self):
        self.func = cached(sum1)

    def test_cache_count(self):
        self.assertEqual(self.func.used_cache_count, 0)
        self.func(1, 1)
        self.func(1, 1)
        self.func(1, 1)
        self.assertEqual(self.func.used_cache_count, 2)

    def test_cached(self):
        self.assertEqual(self.func(10, 10), 20)
        


#-------------------------------------------------------------------#
# pytest
#-------------------------------------------------------------------#
def test_not_str_decorator():
    with pytest.raises(ValueError):
        global sum1
        sum1 = not_str(sum1)
        sum1("1", 2)


#-------------------------------------------------------------------#
# parametrize test (7 тестов)
#-------------------------------------------------------------------#
params = [
    (0, 10, 10),
    (10, 10, 20),
    (-100, 90, -10),
    (20, 80, 100),
]

@pytest.mark.parametrize("a,b,expected", params)
def test_not_str(a, b, expected):
    global sum1
    sum1 = not_str(sum1)
    assert sum1(a, b) == expected


@pytest.mark.parametrize("a,b,expected", params)
def test_divisor_of_one_hundred(a, b, expected):
    global sum1
    sum1 = divisor_of_one_hundred(sum1)
    assert sum1(a, b) == expected


#$ python -m pytest homework11_tests.py
#=================================================== test session starts ====================================================
#platform win32 -- Python 3.9.4, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
#rootdir: C:\Users\valen\Documents\programms\hillel_homework\homework
#collected 11 items
#
#homework11_tests.py ...........                                                                                       [100%]
#
#==================================================== 11 passed in 0.14s ==================================================== 