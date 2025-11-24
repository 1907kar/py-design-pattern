class Person:
    def __init__(self):
        self.name = None
        self.age = None
        self.location = None
    
    def __str__(self):
        return f"{self.name} aged {self.age} from {self.location}"

        
class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person
    
class PersonalBuilder(PersonBuilder):
    def called_as(self, name):
        self.person.name = name
        return self

class AgeBuilder(PersonalBuilder):
    def aged(self, age):
        self.person.age = age
        return self
    
class LocationBuilder(AgeBuilder):
    def born_at(self, location):
        self.person.location = location
        return self
    
pb = LocationBuilder()
karthik = pb\
            .called_as("karthik")\
            .aged("35")\
            .born_at('Tenkasi')\
            .build()
print(karthik )