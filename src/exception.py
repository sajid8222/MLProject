import sys  # Import the sys module to access system-specific functions and parameters.
import logging
# Function to generate detailed error messages
def error_message_detail(error, error_detail: sys):
    """
    This function captures the detailed error message, including:
    - The file name where the error occurred.
    - The line number in the file where the error occurred.
    - The original error message.

    Parameters:
        error (Exception): The original exception object.
        error_detail (sys): The sys module to extract exception information.

    Returns:
        str: A formatted error message with the script name, line number, and error description.
    """
    _, _, exc_tb = error_detail.exc_info()  # Extract traceback information (type, value, traceback).
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the filename from the traceback object.
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)  # Format the error message with script name, line number, and error.
    )
    return error_message  # Return the detailed error message.

# Custom exception class to handle and format exceptions
class CustomException(Exception):
    """
    A custom exception class that inherits from Python's built-in Exception class.
    This class provides detailed error messages for debugging purposes.

    Attributes:
        error_message (str): The detailed error message generated using error_message_detail.
    """

    def __init__(self, error_message, error_detail: sys):
        """
        Constructor to initialize the CustomException.

        Parameters:
            error_message (str): The original error message.
            error_detail (sys): The sys module to extract exception details.
        """
        super().__init__(error_message)  # Call the parent Exception class constructor with the error message.
        self.error_message = error_message_detail(error_message, error_detail=error_detail)  # Generate the detailed error message.
    
    def __str__(self):
        """
        String representation of the exception. When the exception is printed,
        this method returns the detailed error message.

        Returns:
            str: The detailed error message.
        """
        return self.error_message  # Return the formatted error message.

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e, sys)
