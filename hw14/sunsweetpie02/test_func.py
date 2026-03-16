import unittest
import functions
import functions_with_errors


def manual_tests(module):
    try:
        if module.greeting_by_name("Siuzanna") == "Hello Siuzanna!":
            print("Test greeting_by_name(name) is Passed")
        else:
            print("Test greeting_by_name(name) is Failed")
    except:
        print("Test greeting_by_name(name) is Failed")

    try:
        if module.get_symbol_position("banana", "ba") == "Error! Symbol can be string with only one letter":
            print("Test get_symbol_position(text, symbol) when symbol incorrect is Passed")
        else:
            print("Test get_symbol_position(text, symbol) when symbol incorrect is Failed")
    except:
        print("Test get_symbol_position(text, symbol) when symbol incorrect is Failed")

    try:
        if module.get_symbol_position("banana", "n") == 3:
            print("Test get_symbol_position(text, symbol) with success is Passed")
        else:
            print("Test get_symbol_position(text, symbol) with success is Failed")
    except:
        print("Test get_symbol_position(text, symbol) with success is Failed")

    try:
        if module.get_symbol_position("banana", "z") == "Not found":
            print("Test get_symbol_position(text, symbol) when symbol was not found is Passed")
        else:
            print("Test get_symbol_position(text, symbol) when symbol was not found is Failed")
    except:
        print("Test get_symbol_position(text, symbol) when symbol was not found is Failed")

    try:
        d1 = {"a": 5}
        module.merge(d1, {"b": 7})
        if d1 == {"a": 5}:
            print("Test merge(dict1, dict2) dict1 immutability is Passed")
        else:
            print("Test merge(dict1, dict2) dict1 immutability is Failed")
    except:
        print("Test merge(dict1, dict2) dict1 immutability is Failed")

    try:
        d2 = {"b": 7}
        module.merge({"a": 5}, d2)
        if d2 == {"b": 7}:
            print("Test merge(dict1, dict2) dict2 immutability is Passed")
        else:
            print("Test merge(dict1, dict2) dict2 immutability is Failed")
    except:
        print("Test merge(dict1, dict2) dict2 immutability is Failed")

    try:
        if module.merge({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}:
            print("Test merge(dict1, dict2) is Passed")
        else:
            print("Test merge(dict1, dict2) is Failed")
    except:
        print("Test merge(dict1, dict2) is Failed")


manual_tests(functions)
manual_tests(functions_with_errors)

print("\nUnit tests")


class BaseTest:
    module = None

    def test_greeting(self):
        self.assertEqual(self.module.greeting_by_name("Siuzanna"), "Hello Siuzanna!")

    def test_symbol_incorrect_length(self):
        expected = "Error! Symbol can be string with only one letter"
        self.assertEqual(self.module.get_symbol_position("banana", "ba"), expected)

    def test_symbol_success(self):
        self.assertEqual(self.module.get_symbol_position("banana", "n"), 3)

    def test_symbol_not_found(self):
        self.assertEqual(self.module.get_symbol_position("banana", "z"), "Not found")

    def test_merge_result(self):
        self.assertEqual(self.module.merge({"x": 4}, {"y": 8}), {"x": 4, "y": 8})

    def test_merge_immutability(self):
        d1 = {"x": 4}
        self.module.merge(d1, {"y": 8})
        self.assertEqual(d1, {"x": 4})


class TestFunctions(BaseTest, unittest.TestCase):
    module = functions


class TestErrorFunctions(BaseTest, unittest.TestCase):
    module = functions_with_errors


if __name__ == "__main__":
    unittest.main()