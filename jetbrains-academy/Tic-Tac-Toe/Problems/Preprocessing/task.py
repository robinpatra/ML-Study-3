word = input()

new_word = word.lower()
new_word = new_word.replace(",", "")
new_word = new_word.replace(".", "")
new_word = new_word.replace("!", "")
new_word = new_word.replace("?", "")
print(new_word)
