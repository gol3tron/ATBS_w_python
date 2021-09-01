#import stuffs
import pprint

#define the function
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k,v in inventory.items():
        #fill this part in
        print(str(v) + ' ' + k)
        item_total += v
    print()
    print("Total number of items: "+str(item_total))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if inventory.setdefault(item,1) > 1:
            #means we already have some of this item
            inventory[item] += 1
        else:
            #means we dont have any yet, so add 1
            inventory.setdefault(item,1)

    return inventory

#main program
if __name__ == '__main__':
    #stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    #displayInventory(stuff)

    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    displayInventory(inv)
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)
