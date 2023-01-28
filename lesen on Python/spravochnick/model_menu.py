import model

def select(number):
    if number == 1:
        print(model.new_item())
    elif number == 2:
        print(model.print_spravochnick())
    elif number == 3:
        print(model.item_search())