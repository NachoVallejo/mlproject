import sys
# from logger import logging

def error_message_detail(error, error_detail: sys):
    """
    Constructs a detailed error message including the file name and line number
    where the exception occurred.

    Args:
        error (Exception): The exception object.
        error_detail (sys): The sys module to access exception info.

    Returns:
        str: A formatted error message with details.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    return f"Error occurred in file: {file_name} at line: {line_number} with message: {str(error)}"
class CustomException(Exception):
    """
    A custom exception class that extends the base Exception class to include
    detailed error information.

    Attributes:
        error_message (str): The detailed error message.
    """

    def __init__(self, error, error_detail: sys):
        """
        Initializes the CustomException with a detailed error message.

        Args:
            error (Exception): The original exception.
            error_detail (sys): The sys module to access exception info.
        """
        super().__init__(error)
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self):
        """
        Returns the string representation of the CustomException.

        Returns:
            str: The detailed error message.
        """
        return self.error_message
    
# if __name__ == "__main__":
#     try:
#         1 / 0
#     except Exception as e:
#         logging.info("Divider by zero error occurred.")
#         custom_exc = CustomException(e, sys)
#         print(custom_exc)
