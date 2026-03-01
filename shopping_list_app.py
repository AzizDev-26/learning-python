# Shopping List App

"""
A simple shopping list application.
"""

class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f'Added {item} to the shopping list.')

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f'Removed {item} from the shopping list.')
        else:
            print(f'{item} not found in the shopping list.')

    def view_list(self):
        print('Shopping List:')
        for item in self.items:
            print(f'- {item}')

# Example Usage
if __name__ == '__main__':
    shopping_list = ShoppingList()
    shopping_list.add_item('Milk')
    shopping_list.add_item('Bread')
    shopping_list.view_list()
    shopping_list.remove_item('Milk')
    shopping_list.view_list()