scores = input().split()
# put your python code here

correct_count = 0
incorrect_count = 0

for s in scores:
    if s == "C":
        correct_count += 1
    else:
        incorrect_count += 1

    if incorrect_count == 3:
        break

if incorrect_count < 3:
    print("You won")
else:
    print("Game over")
print(correct_count)
