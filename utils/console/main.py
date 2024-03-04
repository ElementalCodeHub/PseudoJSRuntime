from colorama import Fore, Style, init
from tabulate import tabulate

# Initialize colorama to enable ANSI escape code support on Windows
init()

class Console:
    def __init__(self):
        self.error_message = None  # Instance variable to store error messages

    @staticmethod
    def print_colored_text(text, color):
        """
        Print text in the specified color using colorama.

        Args:
        text (str): Text to be colored.
        color (colorama.Fore): Color code from colorama.Fore module.
        
        Returns:
        str: Colored text.
        """
        colored_text = f'{color}{text}{Style.RESET_ALL}'
        return colored_text

    def log(self, sep="", end="", *x):
        """
        Log messages in the default color.

        Args:
        sep (str, optional): Separator between messages. Defaults to "".
        end (str, optional): String appended after the last message. Defaults to "".
        *x: Variable number of messages.
        """
        if not x:
            print("Undefined")
        else:
            for i in x:
                print(i, sep=sep, end="")
            print(end)

    def set_error(self, error):
        """
        Set the error message.

        Args:
        error (str): Error message to be set.
        """
        self.error_message = error
    
    def error(self, ERROR):
        """
        Print the error message in red.

        Args:
        ERROR (str): Error message to be printed.
        """
        self.set_error(ERROR)
        if self.error_message is not None:
            colored_error = self.print_colored_text(self.error_message, Fore.RED)
            print(colored_error)
        else:
            print("Error not set")

    def warn(self, warning):
        """
        Print a warning message in yellow.

        Args:
        warning (str): Warning message to be printed.
        """
        colored_warning = self.print_colored_text(warning, Fore.YELLOW)
        print(colored_warning)
    
    def table(self, data, headers=None):
        """
        Prints tabular data in a table format.

        Args:
        data (list of dict): List of dictionaries representing rows of data.
        headers (list, optional): List of column headers. Defaults to None.
        """
        print(tabulate(data, headers=headers, tablefmt='orgtbl'))
