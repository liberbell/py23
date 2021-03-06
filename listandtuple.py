immutable_tuple_1 = (0, 1, 2, 3)
print(immutable_tuple_1)

# immutable_tuple_1[0] = 4
# print(immutable_tuple_1)

immutable_tuple_2 = (4, 2, 3, (6, 5))
print(immutable_tuple_2)

# immutable_tuple_2[3][0] = 4
# print(immutable_tuple_2)

immutable_tuple_3 = (4, 2, 3, [6, 5])
immutable_tuple_3[3][0] = 7
print(immutable_tuple_3)

my_tuple = ("P", "y", "t", "h", "o", "n")
print(my_tuple)

# del(my_tuple[3])
# print(my_tuple)
# del(my_tuple)
# print(my_tuple)

tuple_a = (1, 2, 3, 4, 5)
tuple_b = ("a", "b", "c", "d", "e")
print(tuple_a + tuple_b)
zipped = zip(tuple_a, tuple_b)
print(zipped)

result = tuple(zipped)
print(result)

tuple_x, tuple_y = zip(*result)
print("Tuple x: ", tuple_x)
print("Tuple y: ", tuple_y)

list_a = [6, 7, 8, 9, 10]
list_b = ["f", "g", "h", "i", "j"]

zipped_list = zip(list_a, list_b)
print(zipped_list)

result = list(zipped_list)
print(result)

a = ("Jhon", "Charles", "Mike")
b = ("Manager", "Supervisor", "Engineer")
x = zip(a, b)

print(dict(x))

numbers_list = [1, 2, 3]
str_list = ["one", "two", "three"]
numbers_tuple = ("ONE", "TWO", "THREE", "FOUR")

result = zip(numbers_list, numbers_tuple)
print(result)

result_set = set(result)
print(result_set)

result = zip(numbers_list, str_list, numbers_tuple)
result_set = set(result)
print(result_set)