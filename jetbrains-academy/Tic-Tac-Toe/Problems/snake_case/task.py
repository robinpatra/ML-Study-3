string = input()

results = []

for i, char in enumerate(string):
    if i != 0 and char.isupper():
        results.append('_')
    results.append(char.lower())

print("".join(results))
