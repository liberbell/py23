print("World")

x = "World"
print(x)

print(x[0])
print(x[3])

# print(x[6])
# x[0] = "B"
print(x)

a, b, c, d, e = x
print(a)
print(a, b, c, d, e)

# a, b, c, d = x
# print(x)

a, b, _, _, _ = x
print(b)

# print(input("How are you?: "))
# place = input("Where are you from?: ")
place = "New York City"
print(place)
print(len(place))

print(place[:9])

print(place.startswith("N"))
print(place.startswith("n"))
print(place.endswith("y"))
print(place.endswith("City"))

print(place.count("y"))

lower_place = place.lower()
print(lower_place)

upper_place = place.upper()
print(upper_place)

print(upper_place.count("Y"))

print(lower_place == upper_place)

print(place.find("C"))
print(place.find("York"))
print(place.index("Y"))
# print(place.index("c"))
print(place.find("c"))

split_place = place.split("k")
print(split_place)
print(place.count(" "))