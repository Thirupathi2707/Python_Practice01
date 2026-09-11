#Sum of two numbers

def add(a,b):
    return  a+b;

print(add(10,20))

#even or odd

def evenorodd(a):
    if a%2 == 0:
        print("Even")
    else:
        print("odd")

evenorodd(7)

#square

def square(s):
    return s*s;

print(square(5))

#maximum()

def max(c,d):
    if c>d :
       print("c")
    else:
       print("d") 

max(10,25)

#vowels in a string

def vowels(st):
    c = 0
    for i in range(0,len(st)):
        if st[i] == 'a' or  st[i] == 'e' or st[i] == 'i' or st[i] == 'o' or st[i] == 'u':
         c+=1
    return c
        
    
print(vowels("hello"))

#reverse a string

def r(e):
    rev = ""
    for i in range(len(e)-1,-1,-1):
        rev += e[i]  
    return rev

print(r("Python"))

#palindrome

def p(pal):
    palin = ""
    for i in range(len(pal)-1,-1,-1):
        palin += pal[i]
   
   
    if palin == pal:
         return True

    else:
         return False
    
print(p("madam"))

#sum

def sum():
    n = [10,20,30,40]
    sum = 0

    for i in range(0,len(n)):
        sum += n[i]
    return sum

print(sum())

#even or odd

def EorO():
    l = [1,2,3,4,5,6]
    e = 0
    o = 0

    for i in range(0,len(l)):

        if l[i]%2 == 0:
            e += 1
            print("Even: ",e)
        else:
            o += 1
            print("Odd: ",o)

EorO()

#largest number
def large():
    m = [10,45,7,89,23]
    h = m[0]

    for i in range(len(m)):
        if m[i] > h :
           h = m[i]
    return h

print(large())

#duplicate

def dup():
    a = [10,20,10,30,20,40]
    
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] == a[j]:
                a.pop(j)
                break
    return a

print(dup())

#count

def c():
    numbers = [1,2,2,3,4,3]
    e = int(input("Enter a number:  "))
    total = 0
    for i in range(len(numbers)):
        if numbers[i] == e:
            total += 1
    return total
                  
print(c())

#second largest

def sl():
    num = [10, 25, 7, 45, 18]
    hs = num[0]
    for i in range(len(num)):
        if num[i] > hs:
           larges = hs
           hs = num[i] 
           
    return larges

print(sl())

# even and odd separate

def evenorod():
    nums = [1, 2, 3, 4, 5, 6]
    g = []
    h = []
    for i in range(len(nums)):
        if nums[i]%2 == 0:            
           g.append(nums[i])
        else:
            h.append(nums[i])
    print("Even:  ",g)
    print("Odd:  ",h)

evenorod()

#common

def common(): 
    a = [1, 2, 3, 4]
    b = [3, 4, 5, 6]
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                c.append(b[j])
                
    print("common elements:  ",c)
    
common()

#double numbers

def double():
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda n:n+n, numbers))
    print(result)

double()

#square
numbers = [2, 3, 4, 5]
result = list(map(lambda n: n*n, numbers))
print(result)

#even
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(filter(lambda n: n%2==0,numbers))
print(result)

#total
from functools import reduce
numbers = [10, 20, 30, 40]
result = reduce(lambda x,y:x+y, numbers )
print(result)