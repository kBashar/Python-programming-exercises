import math

def printnumbers():
    numbers = [] 
    k=1
    for number in range(2000,3201)[::k]:
        if (number%7 is 0) and (number%5 is not 0):
            numbers.append(number) 
            if k is not 7: 
                 k=7;
    print(numbers)

def fact(n):
	fa = 1
	for d in range(n,1,-1):
		fa = fa * d
	return fa;

#n = int(input('Number --> '))
#print(fact(n)) 

#Problem 3, asks to print a dictionary where values are square of the key. n is input.

def sqdic(n):
    return {x: x*x for x in range(1,n+1)}

def sqdic2(n):
    d = {}
    for x in range(1,n+1):
        d[x] = x*x;
    return d
#Problem 4, str split and rsplit methods use

def splitthestr(s):
    print(type(s)) 
    slist = s.split(',')
    print(slist)
    print(tuple(slist))

#sa = input("give numbers")
#splitthestr(sa)

class TestClass:

    def __init__(self, name):
        self.name = name;

    def getwelcomemessage(self):
        print('hello {}'.format(self.name))

#tc = TestClass("Jubayer")
#tc.getwelcomemessage()

# problem 6

def calculateQ(D):
    C = 50
    H = 30
    Q = math.sqrt((2*C*D)/H)
    return math.floor(Q)
def getnumbers(st):
    l = st.split(',')
    nl = [int(x) for x in l]
    return nl

#s = input("--> Numbers: ")
#l = [calculateQ(x) for x in getnumbers(s)]
#l = map(str, l)
#print (','.join(l))

#problem 7

