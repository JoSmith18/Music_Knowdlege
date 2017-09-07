import core


def au_inventory():
    title = []
    with open('auction_inventory.txt', 'r') as file:
        file.readline()
        lines = file.readlines()

    data = map(lambda i: i.split('|'), lines)
    data = [[a.strip(), b.strip(), c.strip()] for a, b, c in data]
    inventory = {i[1].strip(): {} for i in data}

    for name, item_type, items in data:
        inventory[item_type.strip()][name] = list(
            map(lambda s: s.strip(), items.split(',')))
    return inventory