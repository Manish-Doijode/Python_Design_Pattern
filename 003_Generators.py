#Generators return the yield value and next call will proceed from next statement of yoeld

def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5

v_result = infinite_sequence()

print('first',next(v_result))
print(next(v_result))
print(next(v_result))
print(next(v_result))
print(next(v_result))
print(next(v_result))

import sys

def mygenerator(n):
    for i in range(n):
        yield i**2

v_value = mygenerator(10)

for i in v_value:
    print(i)


#v_value = next(mygenerator(100))
#print(v_value)