my_tuple = ()
print(my_tuple)

type(my_tuple)
print(type(my_tuple))

int_tuples = (1, 2, 3)
print(int_tuples)

str_tuples = ("Hello", "World")
print(str_tuples)

print(int_tuples, str_tuples)

combine_tuples = int_tuples + str_tuples
print(combine_tuples)

print(str_tuples * 3)

mixed_tuple = (1, "Hello", 3.4)
print(mixed_tuple)
my_tuples = 1, "Hello", 3.4
print(my_tuples)
a, b, c = my_tuples
print(a)
print(b)
print(c)

nested_tuple = (1, 2, 3, (4, 5, 6))
print(nested_tuple)