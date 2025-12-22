#list -> store multiple data items in a single variable

fruits = ["mango", "banana"]
fruits.append("orange") #adding value at the end of the list
print(fruits)

fruits.insert(2, "grapes") #adding value at the specific index
print(fruits)

fruits.pop()
print(fruits.remove("mango")) #remove specific value from list
print(fruits)

x = fruits.index("banana")  #getting index of specific data 
print(x)

fruits.sort() #sorting the list in ascending order
fruits.reverse() #reversing the list
print(fruits)

fruits.extend(["kiwi","apple"])  #adding multiple values at the end of the list     
print(fruits)

dollor = [222, 333, 444, 500]
dollor.sort() #ascending order
dollor.sort(reverse=True) #sorting in descending order
dollor.reverse() #reversing the list
print(dollor)