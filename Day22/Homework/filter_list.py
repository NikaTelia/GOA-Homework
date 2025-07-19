words = ["Georgia", "America", "Brazil", "USA", "canada", "africa", "Russia"]
short_words = []

for word in words:
    if len(word) < 5:
        short_words.append(word)

print(short_words)

