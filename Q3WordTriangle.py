word = input("Enter a word: ")
word = word.upper()

for i in range(1, len(word) + 1):
    print(word[:i])