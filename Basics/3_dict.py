# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
# print(users)


# user, status = {'Hans', 'active'}
# print(user)
# print(status)

# for i in range(7):
#     if i == 4:
#         break
#     print(f"BREAK: This is after break -- iteration {i}")

# print("BREAK: This is after the program")


# for i in range(7):
#     if i == 4:
#         continue
#     print(f"CONTINUE: This is after break  -- iteration {i}")

# print("CONTINUE: This is after the program")


# for i in range(7):
#     if i == 4:
#         continue
#     print(f"BREAK: This is after break -- iteration {i}")
# else:
#     print("I am from else")


# def whoiam():
#     return True
#     return "I am Goutham"

# print(whoiam())
# print(type(whoiam()))

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

# color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")
#     case Color.BLUE:
#         print("I'm feeling the blues :(")
#     case _:
#         print("None")   


def get_color(color: Color):
    print(Color(color).name)

get_color(Color.BLUE)