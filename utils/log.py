"""# logger.py
The logger module with a function to wrap print statements
"""

import os


def LogFunction(func):
    def wrapper(*args):
        pass  # Temp


file = os.open("logs\\logs.txt", "a")
