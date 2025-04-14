"""
in Java:
public class Item{
    String itemName;
    double itemPrice;

    Item(String itemName, double itemPrice){
    this.itemName = itemName
    this.itemPrice = itemPrice
    }
}
"""

class Item:

    #static variables
    made_in = 'China'
    tariffs = '125%'

# __init__ is build in constructor function
    def __init__(self, item_name, item_price):
        # instance variables
        self.item_name = item_name
        self.item_price = item_price

    # def __str__(self):
    #     return print(f'Item Name: {self.item_name}, Item Price: {self.item_price}')

# built in to string method
    #instance method
    def __str__(self):
        return f'{type(self).__name__} {self.__dict__}'



    def instance_method(self):
        print(f' This is an instance method. Instance methods can interact with instance variables '
              f'of the class  through self keyword like {self.item_name}')

    @staticmethod
    def static_method():
        print(f' This is a static method. Static methods in Python can not interract with class members. '
              f'it is an independent method. Might be used for utilities. Use @classmethod')

    @classmethod
    def class_method(cls):
        print(f'This is a class method which is same as static method in java. This method can interract with class members with cls keyword')
        print(f' This calss method interacts {cls.made_in}')
item1 = Item('Pen', 2)
item2 = Item('Pencil', 1)

print(item1)
print(item2)

#static variables can be called through class name

print(Item.made_in)
print(Item.tariffs)
print("=========== instance method =======")
print(item1.instance_method())
print("=========== static method =======")
Item.static_method()
print("=========== class method cls =======")

Item.class_method()