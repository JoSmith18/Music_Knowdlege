class Items():
    def __init__(category, name, items):
        self.category = category
        self.name = name
        self.items = item
    def __rpr__(self):
        return '{}\n{}\n[{}]\n'.format(self.category, self.name, self.items)

