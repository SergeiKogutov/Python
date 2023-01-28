import model
import view

# def select(number):
#     if number == 1:
#         view.print_days(model.count_days())
#     elif number == 2:
#         view.print_number(model.calculate())
#     elif number == 3:
#         view.print_random(model.random_number())

def count_days():
    return view.print_days(model.count_days())

def calculate_number():    
    return view.print_number(model.calculate())

def create_random_number():
    return view.print_random(model.random_number())