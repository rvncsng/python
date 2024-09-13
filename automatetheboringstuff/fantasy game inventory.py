# Fantasy Game Inventory

def displayInventory(inventory):
    totalItems = 0

    print('Inventory:')
    for itemName, itemAmount in inventory.items():
        print(str(inventory[itemName]) + ' ' + itemName)
        totalItems += inventory[itemName]

    print('Total number of items: ' + str(totalItems) + '\n')

def addToInventory(inventory, addedItems):
    currentItems = list(inventory.keys())
    for addItem in addedItems:
        if addItem not in currentItems:
            inventory[addItem] = 1
        else:
            inventory[addItem] += 1

    return inventory


# inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}
displayInventory(inv)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
