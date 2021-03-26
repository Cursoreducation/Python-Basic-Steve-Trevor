
def sum(a, b):
    print("-sum-")
    c = a + b
    print(f"{a} + {b} = {c}")
    return c


def mul(a, b):
    print("-mul-")
    c = a * b
    print(f"{a} * {b} = {c}")
    return c


c = sum(1, 2)
d = mul(c, 15)

print("d: ", d)