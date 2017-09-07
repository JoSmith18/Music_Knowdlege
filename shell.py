import disk
import core

print('Welcome To TBay Auctions!!\n')
name = input('What is the name for your account customer?\n')
password = input('What will be the password for your profile?\n')
categories = disk.au_inventory()
menu = core.Items(categories)
print(menu)
