def greet(name):
    print('გამარჯობა', name,'!')

greet('nika')

def square(n):
    print(n*n)

square(3)

def even(nums):
    if nums % 2 == 0:
        print('ლუწია')
    else:
        print('კენტია')

even(4)
even(3)

def maximum(a, b, c):
    print(max(a, b, c))

maximum(34, 12, 45)


def maximum(word):
    print(word[::-1])

maximum('python')