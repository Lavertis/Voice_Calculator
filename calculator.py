import re
import random
from audio import *


def calculate(user_input):
    user_input = user_input.replace(',', '.')
    user_input = fix_low_numbers(user_input)
    text = user_input.split()
    operation = ''
    prev = ''
    prev_prev = prev
    numbers = []

    for word in text:
        if word in operation_switcher and is_digit(prev):
            operation = word
        elif is_digit(word):
            if prev == 'minus' and not is_digit(prev_prev):
                numbers.append(-float(word))
            else:
                numbers.append(float(word))
        prev_prev = prev
        prev = word

    try:
        operation_switcher.get(operation)(numbers[0], numbers[1])
    except (IndexError, TypeError):
        say("Nie zrozumiałem tego co powiedziałeś")


def add(x, y):
    result = x + y
    x, y, result = check_if_float(x, y, result)
    synonyms = ('dodać', 'plus')
    text = str(x) + ' ' + random.choice(synonyms) + ' ' + str(y) + ' to ' + str(result)
    say(text)


def subtract(x, y):
    result = x - y
    x, y, result = check_if_float(x, y, result)
    text = str(x) + ' ' + 'odjąć' + ' ' + str(y) + ' to ' + str(result)
    say(text)


def multiply(x, y):
    result = x * y
    x, y, result = check_if_float(x, y, result)
    synonyms = ('pomnożone przez', 'razy')
    text = str(x) + ' ' + random.choice(synonyms) + ' ' + str(y) + ' to ' + str(result)
    say(text)


def divide(x, y):
    try:
        result = x / y
        x, y, result = check_if_float(x, y, result)
        synonyms = ('podzielone przez', 'po podzieleniu przez', 'dzielone przez')
        text = str(x) + ' ' + random.choice(synonyms) + ' ' + str(y) + ' daje ' + str(result)
        say(text)
    except ZeroDivisionError:
        say('Nie można dzielić przez 0!')


operation_switcher = {
    # Addition
    'dodać': add,
    'dodaj': add,
    'dodane': add,
    'plus': add,
    '+': add,

    # Subtraction
    'odjąć': subtract,
    'odejmij': subtract,
    'odjęte': subtract,
    'minus': subtract,
    '-': subtract,

    # Multiplication
    'pomnożyć': multiply,
    'pomnóż': multiply,
    'pomnożone': multiply,
    'razy': multiply,
    'x': multiply,

    # Division
    'podzielić': divide,
    'podziel': divide,
    'podzielone': divide,
}


def fix_low_numbers(user_input):
    numbers = {
        'jeden': '1',
        'dwa': '2',
        'trzy': '3',
        'cztery': '4',
        'pięć': '5',
    }
    for number in numbers:
        user_input = user_input.replace(number, numbers.get(number))
    return user_input


def is_digit(word):
    if re.search('^[+-]?[0-9]+$|^[+-]?[0-9]+[.]?[0-9]+$', word):
        return True


def check_if_float(x, y, result):
    if x.is_integer():
        x = int(x)
    if y.is_integer():
        y = int(y)
    if result.is_integer():
        result = int(result)
    else:
        result = round(result, 2)
    return x, y, result
