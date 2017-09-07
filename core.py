class Items():
    def __init__(self, inventory):
        self.inventory = inventory

    def __rpr__(self):
        return 'Items(Category: '.format(self.inventory.keys())

    def __str__(self):
        menu = 'Menu:\n'
        for items in self.inventory.keys():
            menu += '\n{}\n'.format(items)
        return menu

    # def get_item(self, category):
    #     for items in self.inventory:
    #         if self.inventory == items['Category']:
    #             return items['Items']

    # def idk(item_type):
    #     for names in item_type:
    #         if names == inventory[1]:
    #             # l = {}
    #             # return l.update(names: {inventory[0]: inventory[2] })