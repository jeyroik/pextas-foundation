from pextas.components.item import Item

my_item = Item({"test": 1})
print(my_item)

my_item2 = Item({"test2": 1})

if my_item == my_item2:
    print('Fail')
else:
    print('Is ok')

for i in my_item:
    print(i)

print(my_item.to_dict())

print(my_item.json_encode())