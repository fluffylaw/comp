# Author of this file: Lydia Wang!

file = open("states.txt", "r")
d={}
for line in file:
    x = line.split(",")
    a=x[0]
    b=x[1]
    c=len(b)-1
    b=b[0:c]
    d[a]=b
    
def bluesclues(string):
    print d[string]
