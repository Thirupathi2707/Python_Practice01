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

def spaces():
    f = "Hello World Python"
    p = ""
    for i in range(len(f)):
        if f[i] != " ":
            p += f[i]
    return p

print(spaces())

def long():
    inp = "Python is powerful"
    n = inp.split()
    high = n[0]
    for i in range(len(n)):
        if len(n[i]) > len(high) :
            high =  n[i]
    return high

print(long())

def short():
    inp = "Python is powerful"
    n = inp.split()
    short = n[0]
    for i in range(len(n)):
        if len(n[i]) < len(short) :
            short =  n[i]
    return short

print(short())

def occ(s,ch):
    c = 0
    for i in range(len(s)):
        if s[i] == ch:
           c += 1
    return c

print(occ("programming","g"))

def dup(r):
        s = ""
        for i in range(len(r)):
            if r[i] not in s:
                s += r[i]
        return s
                 
print(dup("programming"))

def palin(p):
         s = ""
         for i in range(len(p)-1,-1,-1):
             s += p[i]
       
         if p == s:
           return "True"
         else:
           return "False" 
             

print(palin("madam"))

def is_prime(n):
    if n < 2 :
       return False

    for i in range(2,n):
        if n % i == 0:
           return False

    return True

print(is_prime(9))
print(is_prime(7))

def  fact(n):
     fac = 1
     for i in range(1,n+1):
         fac *= i

     return fac

print(fact(5))

def sl():
    s = [10, 5, 20, 8, 15]
    h = s[0]
    t = s[0]
    for i in range(len(s)):
        if s[i] > h:
            t = h
            h = s[i]

        if s[i] > t and s[i] != h:
            t = s[i]
            
    return t

print(sl())

def dupl():
    a = [1, 2, 2, 3, 4, 4, 5]
    s = []
    for i in range(len(a)):
        if a[i] not in s:
           s.append(a[i])

    return s

print(dupl())

def asc():
    a = [1, 2, 3, 4, 5]
    
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
           return False
    return True

print(asc())

def miss():
    a = [1, 2, 4, 5, 6]

    for i in range(0,6):
        if a[i] != i+1:
            return i+1

print(miss())

def cmn():
    L = [1, 2, 3, 4]
    M = [3, 4, 5, 6]
    N = []
    for i in range(len(L)):
        for j in range(len(M)):
            if L[i] == M[j] :
                N.append(L[i])
    return N

print(cmn())

def fr():
    a = [1, 2, 2, 3, 3, 3]
    seen = []

    for i in range(len(a)):
        if a[i] not in seen:
            c = 0

            for j in range(len(a)):
                if a[i] == a[j]:
                   c += 1
            print(a[i],c)
            seen.append(a[i])

fr()

