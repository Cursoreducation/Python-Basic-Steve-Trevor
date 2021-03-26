


for el in range(10):
    print(el)

# iter = None


while True:
    try:
        a = next(iter)
    except StopIteration:
        break
