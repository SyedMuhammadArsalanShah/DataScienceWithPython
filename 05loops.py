# Looping Examples in Python

# Simple while loop
a = 1
while a <= 10:
    print("arsalan", a)
    a = a + 1

# While loop to check even and odd numbers
b = 1
while b <= 100:
    if b % 2 == 0:
        print("even", b)
    else:
        print("odd", b)
    b = b + 1

# Leap year counter
byear = 1996
counter = 0
while byear <= 2025:
    if byear % 4 == 0:
        print("is leap year", byear)
        counter = counter + 1
    else:
        print("is not leap year", byear)
    byear = byear + 1

print("leap year counts", counter)

# Factorial calculation
i = 2
fact = 1
nnum = int(input("Enter your number: "))
while i <= nnum:
    fact = fact * i
    i = i + 1
print("factorial is =", fact)

# Sum of numbers
i = 1
sum = 0
nnum = int(input("Enter your number: "))
while i <= nnum:
    sum = sum + i
    i = i + 1
print("sum is =", sum)

# Multiplication Table
i = 1
nnum = int(input("Enter your number for table: "))
while i <= 10:
    print(nnum, "x", i, "=", nnum * i)
    i = i + 1

# Iterating through a list using a for loop
students = ["Baneen", "Urooj", "Esha", "Hafsa", "Junaid", "Arshad", "Hamza", "Talha", "Saaria"]
for sa in students:
    print(sa)

# Using range in for loop
for a in range(10):
    print(a)

# Range with start, stop, step
for a in range(10, 20, 4):
    print(a)

# Using continue in loop
for a in range(11):
    if a == 8 or a == 9:
        continue
    print(a)

# Infinite loop with break condition
while True:
    name = input("Enter Your Name: ")
    if name.lower() == "exit":
        break
