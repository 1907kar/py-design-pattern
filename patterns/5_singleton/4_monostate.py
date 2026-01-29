# This is normal class 
class CEO:
    __shared_dict = {
        "name": "John",
        "age": 67
    }

    def __init__(self):
        self.__dict__ = self.__shared_dict

    def __str__(self):
        return f"CEO {self.__dict__["name"]} is at age {self.__dict__["age"]}"
    

ceo1 = CEO()
print(ceo1)

ceo2 = CEO()
ceo2.age = 70

print(ceo1, ceo2, sep="\n")

# This is singleton metaclass creation
class Monostate:

    _shared = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared
        return obj
    
# The is the consumer class
class CFO(Monostate):

    def __init__(self):
        self.name = ''
        self.money_managed = 0

    def __str__(self):
        return f"{self.name} manages {self.money_managed} $"
    

cfo1 = CFO()
cfo1.name = "David"
cfo1.money_managed = 400000

print(cfo1)
cfo2 = CFO()
cfo2.name = "Sam"
cfo2.money_managed = 10000000

print(cfo1, cfo2, sep="\n")