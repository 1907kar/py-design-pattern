class Person:
    def __init__(self):
        self.name = None
        self.age = None
        self.location = None
        self.company = None
        self.work_title = None
        self.salary = None
    
    def __str__(self):
        return f"{self.name} aged {self.age} from {self.location}\
        \n\tworks at {self.company} as {self.work_title} with salary {self.salary}"
    
class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person

    @property
    def build_personal(self):
        return PersonalBuilder(self.person)

    @property
    def build_official(self):
        return OfficialBuilder(self.person)         
    
    def build(self):
        return self.person
    
class PersonalBuilder(PersonBuilder):
    def __init__(self, person=Person()):
        super().__init__(person)

    def called_as(self, name):
        self.person.name = name
        return self
    
    def with_age(self, age):
        self.person.age = age
        return self
    
    def born_at(self, location):
        self.person.location = location
        return self
    
class OfficialBuilder(PersonalBuilder):
    def __init__(self, person=Person()):
        super().__init__(person)

    def works_at(self, company):
        self.person.company = company
        return self
    
    def with_title(self, work_title):
        self.person.work_title = work_title
        return self
    
    def with_salary(self, salary):
        self.person.salary = salary
        return self
    
pb = PersonBuilder()
pb.build_personal.called_as("karthik")\
    .with_age("35")\
    .born_at("Tenkasi")\
    .build_official.works_at("Fabrikam")\
    .with_title("Engineer")\
    .with_salary("25000")

print(pb.build())