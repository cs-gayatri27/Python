name = ["Shyam", "Gita", "Hari", "Rita"]

print(name[1])
print(name[2])

# for loop -> iteration
for i in name:
    print(i)

fruit = ["mango", "orange", "guava"]
for i in fruit:
    print(i)

cars = ["Audi", "Bmw", "Honda"]
for i in cars:
    print(i)

data = 'python'
for i in data:
    print(i)

for i in range(5):
    print(i)

for i in range(1,10):
    print(i)

for i in range(0,10,2):
    print(i)

sum = 0
for i in range(1,5):
    sum = sum + i
    print(sum)  

sum = 1
for i in range(1,10):
    sum = sum + i
print(sum)

# Nested for loop:

for i in range(6): #i loop
    for j in range(4): # j loop
        print("*", end=" ")
    print("\n")

for i in range(1,9):
    for j in range(i):
        print("*", end=" ")
    print("\n")