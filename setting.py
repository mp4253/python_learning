# Set

#  It is used to store multiple items in a single variable.

#  It is Unordered, Unchangeable, Unindexed.

#  Duplicates values are not allowed.

#  Sets are written with curly brackets {}.

# Set item can be of any data types.

x = {"apple", "banana", "cherry", "orange"}
print(x)

#  type casting
print(type(x))

# length of the set.

print(len(x))


# Set item can be of any data types.

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)


#  Accessing set items

set1 = {"apple", "banana", "cherry"}

if "banana" in set1:
    print("Yes, it is present.")
else:
    print("No, it i NOT present.")
  

#  Adding items in the set.

set1 = {"apple", "banana", "cherry"}

set1.add("mango")

print(set1)


# To join 2 sets using update() method.

setting_1 = {"apple", "banana", "cherry"}
setting_2 = {"tomato", "brinjal", "potato"}

setting_1.update(setting_2)

print(setting_1)


# To remove single item remove() method.

setting_1 = {"apple", "banana", "cherry"}

setting_1.remove("apple")

print(setting_1)

# Note: If the specific item is not available it displays a Keyerror.  


# To remove single item discard() method.

setting_1 = {"apple", "banana", "cherry"}

setting_1.discard("apple")

print(setting_1)

# Note: If the specific item is not present it DOES NOT DISPLAY ERROR.


# To remove single item pop() method.

setting_1 = {"apple", "banana", "cherry"}

setting_1.pop()

print(setting_1)

# Note: This method is used but IT POPS RANDOMLY.


# clear() method is used to clear the set means empty set.

setting_1 = {"apple", "banana", "cherry"}

setting_1.clear()

print(setting_1)


# del keyword is used to delete the set permanently.

setting_1 = {"apple", "banana", "cherry"}

del setting_1

print(setting_1)
