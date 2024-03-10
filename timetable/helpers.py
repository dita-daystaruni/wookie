# contains helper functions
from openpyxl import load_workbook
from datetime import datetime


def parse_nursing_timetable(path_to_file):
    # holds start and end times of every column number
    time_dictionary = {
        "2": ("8AM", "9AM"),
        "3": ("9AM", "10AM"),
        "4": ("10AM", "11AM"),
        "5": ("11AM", "12PM"),
        "6": ("12PM", "1PM"),
        "7": ("1PM", "2PM"),
        "8": ("2PM", "3PM"),
        "9": ("3PM", "4PM"),
        "10": ("4PM", "5PM"),
        "11": ("5PM", "6PM"),
    }

    days_of_the_week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
    unnecessary_course_values = ["CHAPEL", "CLP", "SDL", "KEY", 
                                "CLP-CLINICAL PRACTICE",
                                "SDL- SELF DIRECTED LEARNING"]

    courses = [] # will hold dictionaries of courses

    # loading the excel workbook
    wb_obj = load_workbook(filename="Course_TimeTable.xlsx")
    work_sheets = wb_obj.sheetnames # getting available work sheets

    # getting info from from first workbook
    first_work_sheet = wb_obj[work_sheets[0]]

    # will hold course names and lecturers key being course code
    course_lectures = {}

    # iterating through the sheet
    for row in first_work_sheet.iter_rows(values_only=True):
        if row[1] == "CODE" or row[1] is None:
            continue

        # concantenating course name and the lecturer
        course_lectures[row[1]] = [row[2] , row[3]] 

    second_work_sheet = wb_obj[work_sheets[1]]

    # course contents
    day = ""
    venue = ""
    course_time = ""
    course_name = ""

    # itearating the workbook
    for row_idx, rows in enumerate(second_work_sheet.iter_rows(values_only=True)):
        # skipping the unnecessary titles
        if row_idx in [0, 1, 2]:
            continue

        # skipping row with dates and taking the day of the course
        if rows[1] in days_of_the_week:
            day = rows[1]
            continue

        for idx ,row_value in enumerate(rows):
            # skipping the cohort part
            if idx == 1:
                continue

            # skipping unnecessary course values
            if row_value is None or row_value.strip() in unnecessary_course_values:
                continue

            # getting the venue
            if idx == 0:
                venue = row_value
                continue

            # getting course time
            start_time = time_dictionary[f"{idx}"][0]

            # setting course code
            course_name = row_value.strip()

            # handling merged rows
            remaining_cells = rows[idx+1:]
            last_none = 0
            for rem_idx, rem in enumerate(remaining_cells, start=idx):
                if rem is not None:
                    break

            # concatenating start time and end time
            course_time = start_time + "-" + time_dictionary[f"{rem_idx}"][1]
            
            courses.append({
                "course_code": course_name[:7],
                "lecturer": course_lectures[course_name[:7].strip()][1],
                "course_name": course_name,
                "day":day,
                "venue":venue,
                "time":course_time
                })
    return courses
