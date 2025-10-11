# print -- ეკრანზე გაჩვენებს პასუხს 
# return -- ფუნქციას აბრუნებს პასუხს თვით მნიშვენობას (ჯერ არ აჩვენებს ეკრანს თითომ ამ კოდის პასუხს ნახოლობს)

#---classwork N2---
def sum(a, b, c):
    return a + b + c
print(sum(10, 20, 30))

#---classwork N3---
def substract(a, b):
    return a - b
print(substract(20, 10))

#---classwork N4---
def multiply(a, b):
    return a * b
print(multiply(5, 5))


#---classwork N5---
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "error"
    
print(divide(4, 2))
print(divide(4, 0))