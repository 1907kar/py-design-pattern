# i = 5

# def f(arg=i):
#     print(arg)

# i = 6
# f()


# def f(a, L=[]):
#     L.append(a)
#     print(L)

# f('a')
# f(2, [8])
# f(3, [9, 7])
# f('b')

name="Karthik"
message = "Hello"
def say_hi(greet=message, title=name):
    print(greet, title)

name="Goutham"
say_hi("hi")
