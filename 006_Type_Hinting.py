# need to install mypy to use below -> int
def myfunction1(myparameter : int):
    print(myparameter)

#myfunction1('manish1')
myfunction1(100)

#myfunction('manish')
# if you call above procedure with string value, you will get bwlow error

#(venv) C:\Python_Project\DesignPatterns>mypy 006_Type_Hinting.py
#006_Type_Hinting.py:7: error: Name "myfunction" is not defined  [name-defined]
#Found 1 error in 1 file (checked 1 source file)


def myfunction2(myparameter : int) -> str:
    print(f"{myparameter + 10}")

#myfunction1('manish1')
myfunction1(100)

print(myfunction2(200))

def myfunction3(myparameter : int):
    print(myparameter)

#myfunction1('manish1')
myfunction1(100)

print(myfunction2(200))

print(myfunction3(myfunction2(200)))
# above print will give error because myfunction3 is expecting int, but myfunction2 returns str
