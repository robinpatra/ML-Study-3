vowels = 'aeiou'
# create your list here
word = input()

result = [char for char in word if char in vowels]
print(result)
