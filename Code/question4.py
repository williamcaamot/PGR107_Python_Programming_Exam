import random

def generate_numbers():
    numbers = []
    for x in range(10):
        numbers.append(random.randint(1, 50))
    return numbers


def substitute(numbers):
    new_numbers = []
    for x in numbers:
        if not x % 5:
            new_numbers.append(x * x)
        else:
            new_numbers.append(x)
    return new_numbers