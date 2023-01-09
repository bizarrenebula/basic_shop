class TShirt:
    def __init__(self, color='White', size='M'):
        self.type = 'T-Shirt'
        self.color = color
        self.size = size
        self.price = 15.00

    def __str__(self):
        return f'{self.color} {self.type} {self.size} ${self.price}'


class Jeans:
    def __init__(self, color='Blue', size='M'):
        self.type = 'Jeans'
        self.color = color
        self.size = size
        self.price = 45.00

    def __str__(self):
        return f'{self.color} {self.type} {self.size} ${self.price}'


class Shop:
    def __init__(self, name):
        self.name = name
        self.clothes = {
            'T-Shirt': {'count': 0, 'items': []},
            'Jeans': {'count': 0, 'items': []}
        }

    def addItem(self, item):
        if item.type in self.clothes:
            self.clothes[item.type]['items'].append(item)
            self.clothes[item.type]['count'] += 1
            print(f'{item.type} added to stock')
        else:
            self.clothes[item.type] = {'count': 1, 'items': [item]}
            print(f'{item.type} was added as category')

    def listItems(self):
        print(vars(self))


if __name__ == "__main__":

    # initialize the shop
    shop = Shop('Zara')

    # list available items | output -> {'name': 'Zara', 'clothes': {'T-Shirt': {'count': 0, 'items': []}, 'Jeans': {'count': 0, 'items': []}}}
    shop.listItems()

    # create a t-shirt and print details | output -> Red T-Shirt XL $15.0
    t1 = TShirt('Red', 'XL')
    print(t1)

    # add t-shirt t1 to stock | output -> T-Shirt added to stock
    shop.addItem(t1)

    # list shop items after adding t1
    # output -> {'name': 'Zara', 'clothes': {'T-Shirt': {'count': 1, 'items': [<__main__.TShirt object at 0x000002EB1BD9FD90>]}, 'Jeans': {'count': 0, 'items': []}}}
    shop.listItems()

    # create jeans and print details | output -> Blue Jeans S $45.0
    j1 = Jeans(size='S')
    print(j1)

    # add jeans j1 to stock | output -> Jeans added to stock
    shop.addItem(j1)

    # list shop items
    # {
    # 'name': 'Zara',
    # 'clothes':
    # {
    # 'T-Shirt': {
    # 'count': 1, 'items': [<__main__.TShirt object at 0x000002EB1BD9FD90>]},
    # 'Jeans': {
    # 'count': 1, 'items': [<__main__.Jeans object at 0x000002EB1BD9FD30>]}}
    # }
    shop.listItems()
