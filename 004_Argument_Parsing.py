#def myfunction(*args, **kwargs):
#    print(args[0])
#    print(args[1])
#    print(args[2])
#    print(args[3])
#    print(kwargs['keyone'])
#    print(kwargs['keytwo'])

#myfunction('t1','1',True,'wow',keyone = 'manish',keytwo = '12345')

###################################################################

#import sys

#print(sys.argv[0])#is the filename
#print(sys.argv[1]) #prints first arguments
#print (sys.argv) #prints filename and entire list of arguments

#(venv) C:\Python_Project\DesignPatterns>python 004_Argument_Parsing.py 'a','d'
#004_Argument_Parsing.py
#'a','d'

#(venv) C:\Python_Project\DesignPatterns>python 004_Argument_Parsing.py "hello world" new
#004_Argument_Parsing.py
#hello world
#['004_Argument_Parsing.py', 'hello world', 'new']

#filename = sys.argv[1]
#print(filename)
#message = sys.argv[2]
#print(message)

#with open(filename, 'w+') as f:
#    f.write(message)

#(venv) C:\Python_Project\DesignPatterns>python 004_Argument_Parsing.py message.txt "hello world"
#004_Argument_Parsing.py
#message.txt
#['004_Argument_Parsing.py', 'message.txt', 'hello world']
#message.txt
#hello world

import sys
import getopt

opts, args = getopt.getopt(sys.argv[1:],"f:m:a:b:c:") # f is filename m is message

message = 'no msg'
message1 = 'no msg'

for opt, arg in opts:
    if opt == '-f':
        fn = arg
    elif opt == '-m':
        message = arg
    else:
        message1 = arg

print('opts=',opts)
print('args=',args)

print(fn)
print(message)


##(venv) C:\Python_Project\DesignPatterns>python 00
##4_Argument_Parsing.py "hello world" "how are you"
##
##[]
##['hello world', 'how are you']
##
##(venv) C:\Python_Project\DesignPatterns>python 00
##4_Argument_Parsing.py -m "hello world" -f "how ar
##e you"
##[('-m', 'hello world'), ('-f', 'how are you')]
##[]
##
##(venv) C:\Python_Project\DesignPatterns>python 00
##4_Argument_Parsing.py -m "hello world" -f "how ar

##e you" "this one"
##[('-m', 'hello world'), ('-f', 'how are you')]
##['this one']
##
##(venv) C:\Python_Project\DesignPatterns>

##(venv) C:\Python_Project\DesignPatterns>python 004_Argument_Parsing.py -f "hello world" -m "how are you" -a "this one" -b "b one" -c "trying c"
##[('-f', 'hello world'), ('-m', 'how are you'), ('-a', 'this one'), ('-b', 'b one'), ('-c', 'trying c')]
##[]
##
##(venv) C:\Python_Project\DesignPatterns>

