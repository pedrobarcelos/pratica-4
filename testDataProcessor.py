import os
import unittest
from dataProcessor import read_json_file, avgAgeCountry

class TestDataProcessor(unittest.TestCase):
    def test_read_json_file_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")
        data = read_json_file(file_path)
        self.assertEqual(len(data), 1000)
        self.assertEqual(data[0]['name'], 'Alice')
        self.assertEqual(data[1]['age'], 39)

    def test_read_json_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_json_file("non_existent.json")

    def test_read_json_file_invalid_json(self):
        with open("invalid.json", "w") as file:
            file.write("invalid json data")
        with self.assertRaises(ValueError):
            read_json_file("invalid.json")

    def test_avgAgeCountry_empty_data(self):
        data = []
        avg = avgAgeCountry(data)
        self.assertIsNone(avg)

    def test_avgAgeCountry_missing_age(self):
        data = [
            {"name": "Alice", "country": "US"},
            {"name": "Bob", "country": "UK"},
        ]
        avg = avgAgeCountry(data)
        self.assertIsNone(avg)

    def test_avgAgeCountry_missing_country(self):
        data = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
        ]
        avg = avgAgeCountry(data)
        self.assertIsNone(avg)

    def test_avgAgeCountry_with_age_transformation(self):
        data = [
            {"name": "Alice", "age": 30, "country": "US"},
            {"name": "Bob", "age": 25, "country": "US"},
        ]
        # Define a simple transformation function (age in months)
        def transform_age(age):
            return age * 12
        avg = avgAgeCountry(data, transform_func=transform_age)
        self.assertEqual(avg, {"US": 420.0})

if __name__ == '__main__':
    unittest.main()
