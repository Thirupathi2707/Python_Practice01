# s = "madam"
# reverse = ""

# for i in range(len(s)-1,-1,-1):
#     reverse += s[i]
   
# if  reverse == s:
#     print("palindrome")
# else:
#     print(" not palindrome")       

# s = input("Enter  a string:  ")
# c = s.split()

# for i in range(len(c)):
#     print(c[i], end= "")

# Find the largest element in a list without using max().
# numbers = [10, 25, 7, 45, 18]
# Find the smallest element without using min().
# Find the sum of all elements without using sum().
# Count the number of even and odd numbers in a list.
# Reverse a list without using reverse() or [::-1].
# Remove duplicate elements from a list.

# Output: 40
# Find the second smallest number in a list.
# Count how many times a given number appears in a list without using count().
# Separate a list into two lists: even numbers and odd numbers.

# Example:

# Input:
# [1, 2, 3, 4, 5, 6]

# Output:
# Even: [2, 4, 6]
# Odd:  [1, 3, 5]
# l = [1, 2, 2, 3, 4, 4, 5]
# s = int(input("Enter a number: "))
# c = 0

# for i in range(0,len(l)):
#      if l[i] == s:
#         c+= 1    

# print(c)


l = [1, 2, 3, 4, 5, 6,7]
e = []
o = []

for i in range(0,len(l)):
    if l[i] % 2 == 0:
        e.append(l[i])
        
    else:
        o.append(l[i])
       
print(e)
print(o)










