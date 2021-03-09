import pickle


# list_1 = [1, 2, 3, 4, 5, 6]

# file = open("test.txt", "w")
#
# list_1_b = pickle.dumps(list_1)
# file.write(str(list_1_b))
# file.close()


file = open("test.txt", "r")

list_1_b = file.read()
print(list_1_b)
list_1 = pickle.loads(bytes(list_1_b))
print(list_1)
file.close()







