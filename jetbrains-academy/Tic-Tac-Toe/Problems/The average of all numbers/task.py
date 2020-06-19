# put your python code here
a = int(input())
b = int(input())

count = 0
sum_div_of_3 = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        count += 1
        sum_div_of_3 += i

print(sum_div_of_3 / count)
