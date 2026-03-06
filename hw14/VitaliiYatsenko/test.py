from functions import greeting_by_name
from functions import get_symbol_position
from functions import merge

from functions_with_errors import get_symbol_position


def test_greeting_by_name_correct():
    assert greeting_by_name('Vitalii') == 'Hello Vitalii!'

def test_get_symbol_position_found():
    assert get_symbol_position('Hello', 'e') == 2

def test_get_symbol_many_symbols():
    assert get_symbol_position('Hello', 'ew') == "Error! Symbol can be string with only one letter"

def test_get_symbol_position_not_found():
    assert get_symbol_position('Hello', 'c') == "Not found"

def test_merge_correct():
    dict1 = {
    'name': 'Vitalii',
    'username': 'User123'
    }

    dict2 = {
    'device': 'phone', 
    'time': '1h'
    }

    dict3 = {'name': 'Vitalii',
         'username': 'User123',
         'device': 'phone', 
         'time': '1h'}
    
    assert merge(dict1,dict2) == dict3

def test_merge_overwrite_dict():
    dict1 = {
    'name': 'Vitalii',
    'username': 'User123'
    }

    dict2 = {
    'device': 'phone', 
    'time': '1h'
    }
    assert merge(dict1,dict2) != dict1

tests = [
    test_greeting_by_name_correct,
    test_get_symbol_position_found,
    test_get_symbol_many_symbols,
    test_get_symbol_position_not_found,
    test_merge_correct,
    test_merge_overwrite_dict
]

for test in tests:
    try:
        test()
        print(f'"{test.__name__}" --- passed\n')

    except AssertionError as e:
        print(f'"{test.__name__}" --- failed\n')
        print(e)



import unittest

class TestFunctions(unittest.TestCase):
    def test_greeting_by_name_correct(self):
        self.assertEqual(greeting_by_name('Vitalii'), 'Hello Vitalii!')

    def test_get_symbol_position_found(self):
        self.assertEqual(get_symbol_position('Hello', 'e'), 2)

    def test_get_symbol_many_symbols(self):
        self.assertEqual(get_symbol_position('Hello', 'ewf'), "Error! Symbol can be string with only one letter")

    def test_get_symbol_position_not_found(self):
        self.assertEqual(get_symbol_position('Hello', 'm'), 'Not found')

    def test_merge_correct(self):
        dict1 = {
        'name': 'Vitalii',
        'username': 'User123'
        }

        dict2 = {
        'device': 'phone', 
        'time': '1h'
        }

        dict3 = {'name': 'Vitalii',
         'username': 'User123',
         'device': 'phone', 
         'time': '1h'}
    
        self.assertEqual(merge(dict1,dict2), dict3)
    
    def test_merge_overwrite_dict(self):
        dict1 = {
        'name': 'Vitalii',
        'username': 'User123'
        }

        dict2 = {
        'device': 'phone', 
        'time': '1h'
        }

        self.assertNotEqual(merge(dict1,dict2), dict1)


if "__name__" == '__main__':
    unittest.main()