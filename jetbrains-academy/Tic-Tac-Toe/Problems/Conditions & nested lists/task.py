# the list "students" is already defined

result = [name for [name, grade] in students if grade == "A"]
print(result)
