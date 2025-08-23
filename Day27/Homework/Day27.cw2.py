# homework 4
numbers = []

for i in range(5):
    num = int(input(str(i + 1) + ") შეიყვანეთ რიცხვი: "))
    numbers.append(num) 

print(numbers)

# homework 7
students = []


for i in range(3):
    name = input(str(i + 1) + ") შეიყვანეთ სტუდენტის სახელი: ")
    students.append(name)

students.insert(0, "Teacher")
students.pop()

print(len(students))
print(students)
