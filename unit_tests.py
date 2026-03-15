import functions
import functions_with_errors

def run_tests(module):
    res = module.greeting_by_name("Anzhela")
    status = "Passed" if res == "Hello Anzhela!" else "Failed"
    print(f"Test greeting_by_name(name) is {status}")

    res = module.get_symbol_position("Python", "th")
    status = "Passed" if res == "Error! Symbol can be string with only one letter" else "Failed"
    print(f"Test get_symbol_position(text, symbol) when symbol incorrect is {status}")

    res = module.get_symbol_position("Python", "y")
    status = "Passed" if res == 2 else "Failed"
    print(f"Test get_symbol_position(text, symbol) with success is {status}")

    res = module.get_symbol_position("Python", "z")
    status = "Passed" if res == "Not found" else "Failed"
    print(f"Test get_symbol_position(text, symbol) when symbol was not found is {status}")

    d1, d2 = {"a": 1}, {"b": 2}
    res = module.merge(d1, d2)
    
    print(f"Test merge(dict1, dict2) dict1 immutability is {'Passed' if d1 == {'a': 1} else 'Failed'}")
    print(f"Test merge(dict1, dict2) dict2 immutability is {'Passed' if d2 == {'b': 2} else 'Failed'}")
    print(f"Test merge(dict1, dict2) is {'Passed' if res == {'a': 1, 'b': 2} else 'Failed'}")


# using unittest
import unittest

class Test(unittest.TestCase):
    module = None

    def test_greeting(self):
        self.assertEqual(self.module.greeting_by_name("Anzhela"), "Hello Anzhela!")

    def test_symbol_incorrect_length(self):
        expected = "Error! Symbol can be string with only one letter"
        self.assertEqual(self.module.get_symbol_position("test", "te"), expected)

    def test_symbol_success(self):
        self.assertEqual(self.module.get_symbol_position("apple", "p"), 2)

    def test_symbol_not_found(self):
        self.assertEqual(self.module.get_symbol_position("apple", "o"), "Not found")

    def test_merge_result(self):
        self.assertEqual(self.module.merge({"x": 10}, {"y": 20}), {"x": 10, "y": 20})

    def test_merge_immutability(self):
        d1 = {"x": 1}
        self.module.merge(d1, {"y": 2})
        self.assertEqual(d1, {"x": 1}, "Original dictionary dict1 was modified!")


class TestCorrectFunctions(Test):
    module = functions

class TestErrorFunctions(Test):
    module = functions_with_errors


if __name__ == "__main__":
    print("Manual tests")
    run_tests(functions)
    run_tests(functions_with_errors)

    print("\nUnit tests")
    unittest.main()