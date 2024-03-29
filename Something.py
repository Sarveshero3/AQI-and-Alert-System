from icecream import ic

_=0
while (_ := _ +1)<10:
    ic(_)               #use this in VScode since it colors the text which is
                        # only seen in terminal window
else:
    ic("Good Morning")

""" icecream module is a better version of print and is the best for debuging
meaning we can use it to check iteration results in a simpler way .
go to youtube to understand it better """

# here in loop we used a reductant var i.e _ or anonymous variable

''' and after while loop we used else a way to check if the loop has been fully
iterated or not'''

''' Walrus operator (:=) which came after py 3.8 is helpful mostly in case for
while loop since it makes it one less line for defining var or using the same
var and its result again.'''

# Better and a complex example

def getdata():
    for i in range(10):
        yield i
    yield -1

def process(data):
    print(data)         #some process has been done which we don't know

gen = getdata()       #setting up a generator

while (data := next(gen)) != -1:
    process(data)

# Another Example

def f(x):       #a function that does a complex maths
    return x-1

#results = [f(x) for x in range(10) if f(x) > 3]

result_walrus = [result for x in range(10) if (result := f(x)) >3]
print(result_walrus)


#Argument Unpacking

def num(a,b,c,d):
    print(a,b,c,d)

lst=[1,2,3,4]
num(*lst)       # here * (asterisks) unpacks values in an iterable object


#also in dictionary

values = {
    "key": "5",
    "target": 10
}

def parsevalues(target, key):
    print(key, target)      #key=5 target=10

parsevalues(**values)

from collections import defaultdict

def default():
    return 0

d = defaultdict(default)
a="aaaaabbbbbccccaaa"

for i in a:
    d[i]+=1
print(d)

print("Kavish please do tfhghjg")
print("KAVISH WAS HERE")