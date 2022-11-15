def validate_triangle(a, b, c):
    
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return False
    else:
        return True       
a=3
b=4
c=5
print(a,b,c)
if validate_triangle(a, b, c):
    print("Valid")
else:
    print("Invalid")

def validate_rectangle(d,e,f,g):
    if (d==f and e==g) or (d==e and f==g) or (d==g and e==f):
        return True
    else:
        return False     
d=1
e=2
f=3
g=4
print(d,e,f,g)
if validate_rectangle(d,e,f,g):
    print("Valid")
else:
    print("Invalid")
