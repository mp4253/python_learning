a = ["apple", "banana", "kiwi", "pineapple", "dragon"]
print(a)
print(type(a))

b = [1,2,3] + [4, 5, 6] 
print(b)

c = [1,2,3] * 10
print(c)

d = ("hello my name is abc.")

print(d)
print(type(d))

# here it is used conversion from string to list.

x = list(d)
print(x)

a = ["apple", "banana", "kiwi", "pineapple", "dragon"]
print(a)

# To append means to add item in the list which is added to the END OF THE LIST.
a.append("orange")
print(a)

# To insert an item with POSITION & NAME.
a.insert(2,"papaya")
print(a)


# To delete an item from the specific position.
del a[1]
print(a)


# It is used to length of a List.
print(len(a))


# It is used to access the items in the list.

a = ["apple", "banana", "kiwi", "pineapple", "dragon"]
print(a[2])


# range of indexes
print(a[1:4])


# Check if the Item if Exists or not

a = ['apple', 'papaya', 'kiwi', 'pineapple', 'dragon', 'orange']
if "orange" in a:
    print("Yes, it is present.")
else:
    print("No,it is not present.")
    
    
# change the item name & LIST ALSO ALLOWS DUPLICATE VALUES.

a = ["apple", "papaya", "kiwi", "pineapple", "dragon", "orange"]

a[1:3] = ["orange", "mango"]

print(a)


# OR

a = ["apple", "papaya", "kiwi", "pineapple", "dragon", "orange"]

a.insert(1, "mango")
print(a)


d = ["Brinjal", "Tomato", "Ladyfinger", "Potato"]
print(d)

#extend() method is used to add the list into another list.
a.extend(d)
print(a)


#remove() method is used to remove the items from the list.
a.remove("kiwi")
print(a)


#pop() method is used to pop the items from the list.
a.pop(2)
print(a)


#sort() method is used to sort the alphabetically ascending in order.

a.sort()
print("This is in Ascending Order:",a)


# sort() method is used to sort the alphabetically descending in order only write reverse = True.

a.sort(reverse = True)
print("This is in Descending Order:",a)


# copy() it is used to create copy.

m = a.copy()
print("This is the copy command:",m)
