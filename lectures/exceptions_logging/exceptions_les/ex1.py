
while True:
    str_1 = input()
    if not str_1.isdecimal():
        print("str is not decimal")
        continue
    a = int(str_1)
    print(a)
