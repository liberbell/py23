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