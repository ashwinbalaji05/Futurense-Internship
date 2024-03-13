def is_palindrome(word):
    word = word.replace(" ", "").lower()
    if word == word[::-1]:
        print("Yes, it is a palindrome.")
        count_vowels_consonants(word)
    else:
        print("No, it is not a palindrome.")
        print("Reverse of the word:", word[::-1])

def count_vowels_consonants(word):
    vowels = "aeiou"
    count_vowels = sum(1 for char in word if char in vowels)
    count_consonants = len(word) - count_vowels
    print("Count of vowels:", count_vowels)
    print("Count of consonants:", count_consonants)
word1 = "racecar"
is_palindrome(word1)
