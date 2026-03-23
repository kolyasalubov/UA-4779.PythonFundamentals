import unittest, functions, functions_with_errors


class TestFunction(unittest.TestCase):
    def test_functions_greeting_by_name(self):
        self.assertEqual(functions.greeting_by_name("John"), "Hello John!")

    def test_functions_with_errors_greeting_by_name(self):
        self.assertEqual(functions_with_errors.greeting_by_name("John"), "Hello John!")

    def test_functions_get_symbol_position(self):
        test_cases = [
            ("Hello world!", 'e', 2),
            ("Hello world!", '', 1),
            ("Hello world!", 'el', "Error! Symbol can be string with only one letter"),
            ("Hello world!", 'a', "Not found"),
            ("", 'a', "Not found"),
            ("", '', 1),
        ]

        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(functions.get_symbol_position(a, b), expected)

    def test_functions_with_errors_get_symbol_position(self):
        test_cases = [
            ("Hello world!", 'e', 2),
            ("Hello world!", '', 1),
            ("Hello world!", 'el', "Error! Symbol can be string with only one letter"),
            ("Hello world!", 'a', "Not found"),
            ("", 'a', "Not found"),
            ("", '', 1),
        ]

        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(functions_with_errors.get_symbol_position(a, b), expected)

    # def test_functions_get_symbol_position_0(self):
    #     self.assertEqual(functions.get_symbol_position("Hello world!", 'e'), 2)
    #
    # def test_functions_get_symbol_position_1(self):
    #     self.assertEqual(functions.get_symbol_position("Hello world!", ''), 1)
    #
    # def test_functions_get_symbol_position_2(self):
    #     self.assertEqual(functions.get_symbol_position("Hello world!", 'el'), "Error! Symbol can be string with only one letter")
    #
    # def test_functions_get_symbol_position_3(self):
    #     self.assertEqual(functions.get_symbol_position("Hello world!", 'a'), "Not found")
    #
    # def test_functions_get_symbol_position_4(self):
    #     self.assertEqual(functions.get_symbol_position("", 'a'), "Not found")
    #
    # def test_functions_get_symbol_position_5(self):
    #     self.assertEqual(functions.get_symbol_position("", ''), 1)

    def test_functions_merge(self):
        test_cases = [
            ({"name": "John", "age": 25}, {"name": "Anna", "age": 30}, {"name": "Anna", "age": 30}),
            ({"name": "John", "age": 25}, {"city": "New York", "phone": 505787909},
             {'age': 25, 'city': 'New York', 'name': 'John', 'phone': 505787909}),
        ]

        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(functions.merge(a, b), expected)

    def test_functions_with_errors_merge(self):
        test_cases = [
            ({"name": "John", "age": 25}, {"name": "Anna", "age": 30}, {"name": "Anna", "age": 30}),
            ({"name": "John", "age": 25}, {"city": "New York", "phone": 505787909},
             {'age': 25, 'city': 'New York', 'name': 'John', 'phone': 505787909}),
        ]

        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(functions_with_errors.merge(a, b), expected)

    # def test_functions_merge_0(self):
    #     person1 = {"name": "John", "age": 25}
    #     person2 = {"name": "Anna", "age": 30}
    #
    #     self.assertEqual(functions.merge(person1, person2), person2)
    #
    #
    # def test_functions_merge_1(self):
    #     person1 = {"name": "John", "age": 25}
    #     person2 = {"city": "New York", "phone": 505787909}
    #     person_result = {'age': 25, 'city': 'New York', 'name': 'John', 'phone': 505787909}
    #
    #     self.assertEqual(functions.merge(person1, person2), person_result)


if __name__ == '__main__':
    unittest.main()
