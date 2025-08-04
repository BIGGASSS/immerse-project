import os
import random

def clear_screen():
    """
    AI GENERATED CODE
    """
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux (os.name is 'posix')
    else:
        os.system('clear')

def rand_int(a, b):
    return random.randint(a, b)