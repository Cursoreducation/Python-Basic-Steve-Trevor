

class Vector3f:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __mul__(self, other):
        if isinstance(other, Vector3f):
            return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
        elif isinstance(other, (int, float)):
            self.x *= other
            self.y *= other
            self.z *= other

    def __add__(self, other):
        if isinstance(other, Vector3f):
            return Vector3f(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (int, float)):
            self.x += other
            self.y += other
            self.z += other

    def module(self):
        return pow(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2), 0.5)
