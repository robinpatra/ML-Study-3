height = int(input())

result = ""

for i in range(height):
    result += " " * (height - i - 1)
    result += "#" * ((i * 2) + 1)
    result += "\n"

print(result)
