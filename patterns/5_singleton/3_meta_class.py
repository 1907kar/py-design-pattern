class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]
    

class Database(metaclass=Singleton):

    def __init__(self):
        print("This is from init")


d1 = Database()
d2 = Database()
print(d1==d2)