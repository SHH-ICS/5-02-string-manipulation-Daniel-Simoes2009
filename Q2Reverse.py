def reverse_word(word):
    for letter in word[::-1]:
        print(letter)

word = input("Enter a word: ")
reverse_word(word)