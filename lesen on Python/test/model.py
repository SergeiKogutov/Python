import random
import datetime

def count_days():
    current_date = datetime.datetime.now()
    target_date = datetime.datetime(current_date.year, 3, 8)
    return (target_date - current_date).days

def calculate():
    return 2+2

def random_number():
    return random.randint(1, 100)