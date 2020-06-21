words = input()

vowels = "aeiou"
words = words.lower()
for w in words:
    if not w.isalpha():
        break
    print("vowel" if w in vowels else "consonant")
