import string
from random import choice as random_choice


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random_choice(letters) for _ in range(length))
    return random_string
