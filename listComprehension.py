#list comprehension --> consice way to create lists

num = [1,2,3,4,5,6,7,8,9,10]
sq_num = [i**2 for i in num]
cub_num = [i**3 for i in num]
even_num = [i for i in num if i%2 == 0]
odd_num = [i for i in num if i%2 != 0]

print(sq_num)
print(cub_num)
print(even_num)
print(odd_num)

#positive number 
num = [1,2,3,55,-3,-4,-5,-5,66]
pos_num = [i for i in num if i >= 0]
pos_num.sort(reverse=True)
print(pos_num)



birds = ["spaRRow", "pigeon", "eagle", "parrot", "peacock"]
newlist = [i.upper() for i in birds]
newlist2 = [i.lower() for i in newlist]
print(newlist)
print(newlist2)