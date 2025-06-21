number = int(input("შეიყვანეთ ნებისმიერი მთელი რიცხვი: "))
sum = 0

for i in range(1,number + 1):
    sum += i

print(sum)
#--------
number = int(input("შეიყვანეთ ნებისმიერი მთელი რიცხვი: "))
sum = 0

for i in range(1,number + 1,2):
    sum += i

print(sum)