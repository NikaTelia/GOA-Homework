def greet(name):
    print('გამარჯობა', name,'!')

greet('nika')

def square(n):
    print(n*n)

square(3)

def is_even(n):
    if n % 2 == 0:
        print('ლუწია')
    else:
        print('კენტია')

is_even(4)
is_even(3)

def maximum(a, b, c):
    print(max(a, b, c))

maximum(34, 12, 45)


def reverse_text(txt):
    print(txt[::-1])

reverse_text('python')