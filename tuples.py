# Tuples are used to store multiple items in a single variable.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

# Tuples allow duplicates.

# Tuples are immutable.

a = ("apple", "banana", "kiwi", "orange", "pineapple", "dragon")
print(a)
print(type(a))

print(len(a))


if "banana" in a:
    print("Yes, it is present in the tuple.")
else:
    print("No, it is not present in the tuple.")


# Access tuple items

print(a[3])


# to join 2 tuples.
a = ("apple", "banana", "kiwi", "orange", "pineapple", "dragon")
b = ("brinjal", "potato", "tomato", "ladyfinger") 

c = a + b

print(c)


# multiply tuples.
b = ("brinjal", "potato", "tomato", "ladyfinger") 

c = b * 2

print(c)





