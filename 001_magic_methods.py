import math

class person:
    def __init__(self,p_name, p_age):
        self.name = p_name
        self.age = p_age

    def __del__(self):
        print("person Object is deconstructed/deleted")

p = person("manish",25)

class vector1:
    def __init__(self,p_x,p_y):
        self.x = p_x
        self.y = p_y

    def __add__(self, other):
        return vector1(self.x + other.x, self.y + other.y)

    def __del__(self):
        print("vector Object is deconstructed/deleted")

    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"

    def __len__(self):
        self.v_len = int(math.sqrt ((self.x**2) + (self.y**2)))
        return 10 #you can return anything here
        return self.v_len

    def __call__(self, *args, **kwargs):
        print("Hello I was called")

v1 = vector1(10, 20)
v2 = vector1(30,40)
v3 = v1 + v2

print(v3.x, v3.y)

print(v3) #prints values using __repr__

print(type(v3))

print("len:",len(v3))

print(v3.__call__())