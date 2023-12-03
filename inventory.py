def display_inventory(inventory):
    print('Inventory:')
    total_number = 0
    for k, v in sorted(inventory.items()):
        print(f'{v} :{k}')
        total_number += v
    print(f'Totol number of items are {total_number}')

def add_to_inventory(inventory, added_items):
    for added_item in added_items:
        if added_item in inventory:
            inventory[added_item] += 1
        else:
            inventory[added_item] = 1


stuff = {'rope':1, 'torch':2, 'gold coin':42, 'dagger':1, 'arrow':12, }
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'ruby',]
display_inventory(stuff)
add_to_inventory(stuff, dragon_loot)
display_inventory(stuff)