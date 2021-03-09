import pickle


list_1 = {1:"w", 2:"r"}

file = open("test", "wb")
pickle.dump(list_1, file)
file.close()

file = open("test", "rb")

list_2 = pickle.load(file)
file.close()

print(list_2)



