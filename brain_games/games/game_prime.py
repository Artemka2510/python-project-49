import prompt
from random import randint


def is_even_number(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def game_rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def get_answer():
    return prompt.string('Your answer: ')


def get_correct_answer(question):
    return 'yes' if is_even_number(question) else 'no'


def ask_question():
    num = randint(1, 100)
    print('Question:', num)
    return num
