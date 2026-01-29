from random import randint
class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        print("I am from new")
        if not cls._instance: 
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        print(f"I am from init...{randint(1, 100)}")
    
d1 = Database()
d2 = Database()
print(d1 == d2)

class Any:
    pass

a1 = Any()
a2 = Any()
print(a1==a2)