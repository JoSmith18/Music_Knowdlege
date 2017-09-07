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


def add_users(name, password, email):
    with open('user.txt', 'a') as file:
        file.write('{} - {} - {}'.format(name, password, email))


def saved_users():
    names = []
    password = []
    with open('user.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for info in lines:
        info.split('- ')
        names.append(info[0].strip())
        password.append(info[1].strip())
    return names, password