import pendulum
class Items():
    def __init__(self, inventory):
        self.inventory = inventory
        self.bid = 0

    def __repr__(self):
        return 'Items(Category: '.format(self.inventory.keys())

    def __str__(self):
        menu = ''
        for items in self.inventory.keys():
            menu += '\n|{}|\n'.format(items)
        return menu

    def get_brands(self, cat):
        menu = ''
        if cat in self.inventory.keys():
            for items in self.inventory[cat].keys():
                menu += '\n|{}|\n'.format(items)
        return menu

    def get_product(self, cat, brand):
        menu = ''
        if brand in self.inventory[cat].keys():
            for items in self.inventory[cat][brand]:
                menu += '\n|{}|\n'.format(items)
        return menu


class Bidded_Items():
    def __init__(self, item, bid):
        self.item = item
        self.bid = bid
        self.time = pendulum.

    def __str__(self):
        return 'Item: {}, Bid: {}, Time: {}'
