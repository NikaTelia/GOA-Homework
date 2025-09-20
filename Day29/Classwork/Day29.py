grades = []

for i in range(5):
    number = int(input("Please input grade 1-10: "))
    if number < 1 or number > 10:
        print("Error")
    else:
        grades.append(number)

print(grades)


numbers = [5, 12, 7, 9, 20, 33, 41, 56, 78, 91, 100, 121, 150]

even_indexed = numbers[0::2]
odd_indexed = numbers[1::2]
reversed_skip = numbers[::-2]

print(even_indexed)
print(odd_indexed)
print(reversed_skip)




text = "პითონის სლაისინგი მაგარია"

word1 = text[8:17]
phrase = text[:7] + text[17:]
reversed_half = text[::-2]
first_word = text[:-18]

print("\n'სლაისინგი':", word1)
print("'პითონი მაგარია':", phrase)
print("'სლაისინგი მაგარია' (შებრუნებით, ყოველ მეორე ასოზე):", reversed_half)
print("'პითონის':", first_word)