# Dictionaries are used to store data values in key:value pairs.

# Dictionary allows duplicates values.

# empty dictionary
a = {}

b = {"car" : "BMW",
     "model" : "first model",
     "year" : 2004}

print(b)

print(type(b))


# Accessing items.

print(f"The BMW car model year is:",b["year"])


# Dictionary length

print(len(b))


b = {"car" : "BMW",
     "model" : "first model",
     "year" : 2004}

print(b["car"])

# OR

print(b.get("model"))


print(f"This will print all the KEYS :",b.keys())

print(f"This will print all the VALUES :",b.values())

print(f"This will print BOTH COMBINED KEYS & VALUES in a dictionary:",b.items())

b = {"car" : "BMW",
     "model" : "first model",
     "year" : 2004}

if "car" in b:
    print("Yes, it is present in the dictionary.")
else:
    print("No, it is not present in the dictionary.")
    

# change values in the dictionary.

b = {"car" : "BMW",
     "model" : "first model",
     "year" : 2004}

b["year"] = 2008

print(b)


# adding items in the dictionary.


b = {"car" : "BMW",
     "model" : "first model",
     "year" : 2004,}

# b["year"] = 2008

b["year"] = 2012
b["color"] = "black"

print(b)


# pop() method removes only spcific item.
b.pop("model")

print(b)


#popitem() method removes only single item which will recently inserted/added.

b.popitem()
print(b)





