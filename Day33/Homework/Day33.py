# დადებითი print 
# მარტივია გამოსაყენებლად 
# ეკრანზე ჩანს

# უარყოფიტი print
# არ აბრენებს მნიშვენლობას

# დადებითი return
# უფრო სწორი კოდია
# აბრუნებს კოდს
# უფრო მარტივად გამოვიყენებს მათემთიკურ გამოხსნებზე

#უარყოფითი return
# არ იბიჭდება ეკრანზე ეხლავე
# ფუნქცია მარტო ერთხელ შეგვიძლია გამოვიყენოთ def-ში


def check_age(age):
    if age >= 18:
        return("accept granted")
    else:
        return("access denied")

print(check_age(11))
print(check_age(21))



def user_info(name, surmane, address):
  return "მომხმარებლის სახელი:" + name + " " + "მომხმარებლის გვარი:" + surmane + " " + "მომხმარებლის გვარი:" + address

print(user_info('nika', "telia", "secret"))


def numbs(num1, num2):
    return num1 ** num2
print(numbs(20, 20))


def arithmetic_average(numbers):
    if len(numbers) == 0:
        return 0 
    return sum(numbers) / len(numbers)

nums = [2, 3, 11, 13, 21, 32]
print(arithmetic_average(nums))


