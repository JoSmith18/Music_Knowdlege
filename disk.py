import core 
def au_inventory():
    with open('auction_inventory.txt', 'r') as file:
        file.readline()
        items = file.readlines()
    items = map(lambda i: str(i.split(' | ')), items)
    items = list(map(
        lambda l: {
            'Category': l[0],
            'Name': (l[1]),
            'Items':list(map(lambda s: s.strip(), l[2])),
            },
        items))
    return [ core.Items(items['Category'] )
    print(i