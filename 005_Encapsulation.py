class person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, name):
        self.__name = name

p1 = person('manish',40,'male')

#p1.Name = 'man'
#print(p1.__name)

print(p1.Name)

#p1.Name = 'man' #this will now work now

p1.Name = "man"

print(p1.Name)
#p1.Name("man")
#print(p1.Name)