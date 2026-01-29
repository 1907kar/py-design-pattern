from random import randint
def singleton(class_):
    _instance = {}
    def get_instance(*args, **kwargs):
        if not _instance:
            _instance[class_] = class_.__call__(*args, **kwargs)
        return _instance[class_]
    return get_instance

@singleton
class Database:
    def __init__(self):
        self.session_id = randint(1000000000, 9999999999)
        print(f"I am from init..{self.session_id}")

    @property
    def session(self):
        # print(self.session_id)
        pass

    @session.getter
    def get_session(self):
        print(self.session_id)

    @session.setter
    def set_session(self, custom_session_id):
        self.session_id = custom_session_id

d1 = Database()
d2 = Database()
d3 = Database()
print(d1 == d2)

d1.get_session
d2.get_session
d3.get_session

d3.set_session = 12345678910

d1.get_session
d2.get_session
d3.get_session

    