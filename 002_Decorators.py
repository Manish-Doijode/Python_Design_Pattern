#https://www.youtube.com/watch?v=iZZtEJjQLjQ&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=2

def mydecorator(function):

    def wrapper(*args, **kwargs):
        print("I am decorating your function")
        function(*args, **kwargs)

    return wrapper

# this is how it can be done without decorators

#def hello_world():
#    print("Hello World")

#mydecorator(hello_world)()

@mydecorator
def hello_world(p_name):
    print(f"Hello {p_name}")

hello_world("manish")

## practical example

def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)

        with open('logfile.txt','a+') as f:
            fname = function.__name__
            print (f"{fname} returned value {value} ")
            f.write(f"{fname} returned value {value}")

        return value
    return wrapper

@logged
def add(x, y):
    return x + y

print(add(10 , 30))


