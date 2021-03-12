

# file = open("test.txt")
# file.close()

from ex4 import Open2
#
# with open("test.txt", "w") as file:
#     file.write("Hello")
#
# print("end")

with Open2("test.txt", "w") as file:
    file.write("Hello123111")
    raise NameError


