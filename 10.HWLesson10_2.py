min = int(input("Enter the lower limit of the range of numbers: "))
max = int(input("Enter the upper limit of the range of numbers: "))
number = dict()
for i in reversed(range(min, max + 1)):
    key = i
    number[key] = pow(i, i)
print("My dictionary =", number)
