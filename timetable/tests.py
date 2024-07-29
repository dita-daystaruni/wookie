from django.test import TestCase
from .helpers import parse_school_exam_timetable

class TestGetData(TestCase):
    def setUp(self):
        self.file_path = "final_exam_timetable.xlsx"
        # change this upon every new exams timetable
        # pick courses randomly to assertain the correctness of the algorithm

        # self.expected_results = [
        #     {'course_code': 'MUS219A(A)', 'day': 'TUESDAY 2024-08-13', 'time': '12:30PM-1:30PM', 'venue': 'MUS1', 'hrs': '2'},
        #     {'course_code': 'TPC202A', 'day': 'THURSDAY 2024-08-2024', 'time': '10:00AM-12:00PM', 'venue': 'SB-305', 'hrs': '2'},
        #     {'course_code': 'DICT232A', 'day': 'FRIDAY 2024-08-16', 'time': '2:00PM-4:00PM', 'venue': 'ICT115', 'hrs': '2'},
        #     {'course_code': 'ACS404A', 'day': 'FRIDAY 2024-08-23', 'time': '9:00AM-11:00AM', 'venue': 'ICT115', 'hrs': '2'},
        #     {'course_code': 'PHY111PX', 'day': 'SATURDAY 2024-08-24', 'time': '11:05AM-2:05PM', 'venue': 'LAB301', 'hrs': '3'},
        # ]

    def test_return_type(self):
        result = parse_school_exam_timetable(self.file_path)
        self.assertIsInstance(result, list, "The result should be a list")

    def test_elements_type(self):
        result = parse_school_exam_timetable(self.file_path)
        for item in result:
            self.assertIsInstance(item, dict, "Each element in the list should be a dictionary")

    def test_dictionary_keys(self):
        result = parse_school_exam_timetable(self.file_path)
        for item in result:
            self.assertIn("course_code", item, "Each dictionary should have a 'course_code' key")
            self.assertIn("day", item, "Each dictionary should have an 'day' key")
            self.assertIn("time", item, "Each dictionary should have an 'time' key")
            self.assertIn("venue", item, "Each dictionary should have an 'venue' key")
            self.assertIn("hrs", item, "Each dictionary should have an 'hrs' key")

    def test_non_empty_list(self):
        result = parse_school_exam_timetable(self.file_path)
        self.assertGreater(len(result), 0, "The result list should not be empty")

    # def test_data_content(self):
    #     results = parse_school_exam_timetable(self.file_path)
    #     for result in self.expected_results:
    #         print(result)
    #         self.assertIn(result, results, "The expected dictionary is not in the list of extracted data")
