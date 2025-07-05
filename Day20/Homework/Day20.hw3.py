#---Homework N3---
input = input("შეიყვანე სიტყვა: ")
a = "ა"
e = "ე"
i = "ი"
o = "ო"
u = "უ"
num1 = 0
for word in input:
   num1 += (word == a) + (word == e) + (word == i) + (word == o) + (word == u)
print(num1)