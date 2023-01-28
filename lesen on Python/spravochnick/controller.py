import view
import model_menu

def start():
    view.create_menu()
    select()

def select():
    view.input_number()
    number = int(input())
    model_menu.select(number)