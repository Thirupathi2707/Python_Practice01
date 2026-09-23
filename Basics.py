def greet(name):
    return "Hello " + name

print(greet("Thiru"))

def evenorodd(a):
    if a % 2 == 0 :
        return "Even"
    else:
        return "odd"

print(evenorodd(4))

def posneg(a):
    if a > 0 :
       return "Positive"
    elif a < 0:
         return "Negative"
    else:
        return "Zero"

print(posneg(-9))

def large(a,b):
    if a > b:
        return a
    else:
        return b

print(large(9,7))

def squar(a):
    return a * a

print(squar(6))

def total():
    a = [1,2,3,4]
    s = 0
    for i in range(0,4):
        s += a[i]
    return s

print(total())

def  vowels():
    c = 0
    s = "python programming"
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' :
           c += 1
    return c

print(vowels())

def reverse():
    t = "thiru"
    s = ""
    for i in range(len(t)-1,-1,-1):
        s += t[i]
    return s

print(reverse())

def num():
    b = "abc123xyz45"
    c = 0
    for i in range(len(b)):
        if b[i] >= "0" and b[i] <= "9":
            c += 1
    return c

print(num())

def upplow():
    u = "Hello PYthon"
    up = 0
    lo = 0
    for i in range(len(u)):
        if u[i] >= "A" and u[i] <= "Z":
            up += 1
        elif  u[i] >= "a" and u[i] <= "z":
            lo += 1
    return up,lo

print(upplow())

