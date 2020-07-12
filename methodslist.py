list_num = [20, 70, 80, 50, 30, 60, 40]
print(list_num)

print(max(list_num))
print(min(list_num))

print(len(list_num))
list_num.sort()
print(list_num)

list_num.append(25)
print(list_num)

sorted_list_num = sorted(list_num)
print(sorted_list_num)
print(list_num)
print(sum(list_num))
list_num *= 2
print(list_num)

# list_num *= 2.0
# print(list_num)

print(all([0]))
print(all([1]))
print(all([0, 1]))

print(all(list_num))