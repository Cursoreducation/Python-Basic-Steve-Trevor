

# try:
#     file = open("Test.txt")
# except:
#     print("file not exist")
#


while True:
    str_a = input("enter a: ")
    try:
        a = int(str_a)
    except (ValueError, ):
        print("a is not decimal")
        continue

    str_b = input("enter b: ")

    try:
        b = int(str_b)
    except ValueError:
        print("b is not decimal")
        continue

    try:
        c = a / b
    except ZeroDivisionError:
        c = "inf"

    print(f"c: {c}")
