"""
Minion Bot.

Author: Erick Muuo
Description:

The minion bot parses excel files, for timetable and other stuff

Copyright: (C) Academia 2024
"""

import openpyxl


class Minion:
    """Minion.

    Defines funitionality to parse excel files.
    """

    def __init__(self, file: str):
        """Construct a minion instance that parses the excel file."""
        self.file = file

    def is_blankRow(self, columns: iter) -> bool:
        for cell in columns:
            # print(cell)
            if cell.value is not None:
                return False
        return True

    def digest(self):
        """Digest the excel file and return a json object."""
        try:
            wb = openpyxl.load_workbook(filename=self.file)
            sheet = wb.active

            rows = sheet.iter_rows(
                max_row=sheet.max_column,
                min_row=sheet.min_row,
                min_col=sheet.min_column,
                max_col=sheet.max_column,
                # values_only=True,
            )

            for columns in rows:
                if self.is_blankRow(columns):
                    print("blank")
                # if cell.value is not None:
                #     status = str(cell.value)
                # else:
                #     cell.value = status
                # print(cell.value)

        except Exception as e:
            print(e)
