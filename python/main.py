# a = int(input('enter a number'))
# i = 1
# for i in range (1,a+1):
# print('hello world')

# s = "jOhNdOe"
# l = ''
# u = ''
# for i in s:
# if i.islower():
# l = l + i
# else:
# u += i
# print(l+u)

# s = 'P@#yn26at^&i5ve'
# c = 0
# d = 0
# sy = 0
# for i in s:
# if i.isalpha():
# c = c+ 1
# elif i.isdigit():
# d = d + 1
# else:
# sy = sy + 1
# print(f"chars = {c}\ndigits = {d}\nsymbol = {sy}")


# a = int(input("num : "))
# for i in range(1,10+1,1):
#     print(f"{a} x {i} = {a*i}")

#  LIST
# 1. indexing can be done in lists.
# 2. lists can also be directly iterate.
# 3. list is sequential datatype.
# 4. data will be separated by comas.
# 5. list is collection of heterogenous(different kinds of data) datatypes.
# 6. multiple lists can be collected in a single list.
# l = [] # empty list is represented by[]
# print(type(l))

# l = [1,'hello',True,1.1,[2,5],'boy']
# print(l[1:4:1])
# del l[1],l[2]
# # l[0] = 12
# print(l)

# primitive , non-reference,immutable all 3 are not able to change the original data.
# non-primitive,refrences,mutable all 3 are able to change the original data.

# numbers = [2,7,9,11,3]
# numbers.sort()
# numbers.reverse()
# print(numbers[0:2])
# print(min(numbers))
# print(max(numbers))

# john=nhoj = palendrome
# naman=naman = palendrome
# s = 'naman'
# m = ''
# for i in s[::-1]:
# m+=i
# print(s == m)

# s='naman'
# m=''
# for i in range(len(s)-1,-1,-1):
# m+= s[i]
# print(s==m)

# n = 11
# sum = 0
# for i in range(1,n+1,1):
# sum = sum + i
# print(sum)
# print(n*(n+1)/2)

# n = 5
# f = 1
# for i in range(1, n+1,1):
# f = f * i
# print(f)

#  Functions
# 1. parameterized functions
# 2. non-parameterized functions

# def greet():
# print('hello')    # non parameterrized function
# greet()
# greet()

# def sum(a,b):
# print(a+b)      # parameterized function
# sum(2,3)

# def sum(a,b):
#     return a+b
# print(sum(12,3))
# print(sum(12,7))
# print(sum(12,7))
# print(sum(12,2))
# print(sum(12,3))
# print(sum(17,7))
# print(sum(15,7))
# print(sum(14,7))
# print(sum(18,7))
# print(sum(42,7))

# list=[1,2,4,6,8,9,10]
# a = 'bahinkelandbhosdewalde'
# new_a = " "
# for i,v in enumerate(a):
# if i % 2 == 0:
# new_a += v.upper()
# else:
# new_a += v

# prin.t(new_a)

# a = 0
# while a <= 10:
# print(a)
# a+=1

# a = int(input('enter a table: '))
# for i in range(1,11):
#     print(f'{a} X {i} = {a*i}')


# s = 'PraNshUl'
# lower = ""
# upper = ""
# for i in s:
#     if i.islower():
#         lower += i
#     else:
#         upper += i

# print(lower+upper)


# str = "P@#yn26at^&i5ve"
# a = 0
# n = 0
# s = 0
# for i in str:
#     if i.isalpha():
#         a+=1
#     elif i.isdigit():
#         n+=1
#     else:
#         s+=1
# print(a)
# print(n)
# print(s)

# a = int(input('enter a number'))
# for i in range(1,a+1):
#     print(i)

# a = int(input('enter a number'))
# for i in range(a,-1,-1):
#     print(i)


# s = 'hellO WoRld'
# x = ''
# for i in s:
#     if i.islower():
#         x = x+i
# for i in s:
#     if i.isupper():
#         x = x+i
# print(x)

# a = 'pranshul'
# for i in a[::-1]:
#     print(i)

# Python code to demonstrate string length
# using for loop

# Returns length of string

# def findlen(str):
#     counter = 0
#     for i in str:
#         counter +=1
#     return counter

# str = 'pranshul'
# print(findlen(str))


# a =int(input('enter a number'))
# for i in range(a,-1,-1):
#     print(i)


# a = "prapshul"
# b = "pranshul"
# if a == b:
#     print("same")
# else:
#     print("not same")

# if len(a) == len(b):
#     for i in range(0,len(a)):
#         if a[i] == b[i]:
#             print(f"{a[i]} is equal to {b[i]}")
#             continue
#         else:
#             print(f"{a[i]} is not equal {b[i]}")

#             print("not same")
#             break

# else:
#     print("not same")



# pure functions and impure functions : functions which use values within their scope are called pure functions and vice versa.



# x = 2 
# def sum(a,b):
#     global x 
#     x = 3
#     return (a+b)*x
# e = sum(1,3)
# print(e)
# print(x)

# 1 create a function with a variable length length of arguments

# def hobbies(name , age , *a):
#     print(name , age ,a)

# hobbies('john',1 ,3,4,5,67,7,8,)

# 2 return multiple values from a function

# def sum(a , b):
#     op = a+b
#     total = 5 + 5
#     return op,total
# x = sum(2,4)
# print(x)

# 3 create function with a deafault arguments
def dets(name,age,batchcode='p8'):
    print(name,age,batchcode)

dets('john',22)





















