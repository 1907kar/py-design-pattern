class Address:
    def __init__(self, door_no, street, contry):
        self.door_no = door_no
        self.street = street
        self.contry = contry

    def __str__(self):
        return f"\n{self.door_no},\n{self.street},\n{self.contry}"


class Person:
    def __init__(self, name: str, address: Address) -> None:
        if not isinstance(address, Address): #only of instance type Address can be passed
            raise TypeError(f"{address} must be an instance of Address\
                            \nbut this is a {type(address)}")
        self.name = name
        self.address = address

    def __str__(self):
        return f"The person {self.name} lives in the address {self.address}"
    
# john = Person("John", "Abc, londonroad, london")
# print(john)
john = Person("John", Address(25, "2nd cross, sovineur road, London", "England"))
print(john)

# shallow copy, just copies only person object not its used object Address
from copy import copy
# deep copy, recursively copies all its used objects
from copy import deepcopy
jane = copy(john)
jane.name = "Jane"
print(jane)
jane.address.door_no = 45
print(jane)
print(john) #since address object is shallow copied, hence it has changed for john as well as. As this is a reference 
# inorder to do a proper copy of objecs use deepcopy
jane = deepcopy(john)
jane.name = "jane"
jane.address.door_no, jane.address.street, jane.address.contry = 66, "Langlon street, China town", "US"
print(jane)
print(john)
