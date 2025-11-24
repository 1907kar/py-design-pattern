from abc import ABC

class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        return f"The tea is delicious!"
    
class Coffee(HotDrink):
    def consume(self):
        return f"The coffee is delicious!"
    
class TeaFactory(Tea):
    def prepare(self, ml):
        return f"Add {ml} of milk and add required sugar!"

class CoffeeFactory(Coffee):
    def prepare(self, ml):
        return f"Grind some beans, add {ml} if milk and required sugar!"

def make_drink(type):
    if type == ("Tea" or "tea"):
        tp = TeaFactory().prepare(200)
        tc = TeaFactory().consume()
        print(tp, tc)
    elif type == ("Coffee" or "coffee"):
        cp = CoffeeFactory().prepare(50)
        cc = CoffeeFactory().consume()
        print(cp, cc)
    else:
        print("Select only the available drink")

drink = input("Please enter the drink of your choice 'Tea' or 'Coffee': ")
make_drink(drink)
        