import traceback  # To track the error we need traceback library 
import sys

class CustomerException(Exception):  # Custom exception class inheriting from Exception
    def __init__(self, error_message, error_details):
        super().__init__(error_message)  # Inheriting from Exception class
        self.error_message = self.get_details_error_message(error_message, error_details)

    @staticmethod
    def get_details_error_message(error_message, error_details):
        """
        Generates a detailed error message including file name and line number where the error occurred.
        """
        _, _, exc_tb = sys.exc_info()  # Corrected: using sys.exc_info() directly
        if exc_tb is not None:  # To prevent AttributeError in case exc_tb is None
            file_name = exc_tb.tb_frame.f_code.co_filename  # Get the filename where error occurred
            line_number = exc_tb.tb_lineno  # Get the line number where error occurred
            return f"Error Occurred in {file_name}, line {line_number}: {error_message}"
        else:
            return error_message  # Fallback in case no traceback is available

    def __str__(self):
        return self.error_message
