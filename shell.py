import disk
import core

print('Welcome To TBay Auctions!!\n')
name = input('What is the name for your account customer?\n')
password = input('What will be the password for your profile?\n')
categories = disk.au_inventory()
menu = core.Items(categories)
print()
print('\nOkay, Here Are Our Main Catagories\n{}'.format(menu))
cat = input('Which Would You Like To Browse!\n')
print('Which Brand Would You Like To Browse:\n{}'.format(menu.get_brands(cat)))
brand = input('Pick One!\n')
print(menu.get_product(cat, brand))
print('!!The Action End 24hrs After The First Bid!!')
