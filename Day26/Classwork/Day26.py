fruit = ["ვაშლი", "მსხალი", "ატამი", "ბანანი", "ატამი"]
# 0  -- "ვაშლი"
# 1  -- "მსხალი"
# 2  -- "ატამი"
# 3  -- "ბანანი"
# 4  -- "ატამი"
#სულ არის 4 ინდექსი

print(fruit[0])   
print(fruit[-1])


result = []

for i in range(10):
    print(str(i + 1) + ") შეიყვანეთ რიცხვი: ")
    number = int(input())
    if number % 2 == 0:
        result.append(number)

print(str(result))




