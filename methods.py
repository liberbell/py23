cars_list = ["Toyota Camry", "Honda Accord", "Honda Civic", "Toyota Corolla"]

# cars_list[4] = "GM Buick"
cars_list.append("GM Buick")
print(cars_list)

# cars_list.append("Suzuki Vectora", "Nissan Pathfinder")
print(cars_list)
print(len(cars_list))

cars_list.insert(6, "Nissan Pathfinder")
print(cars_list)

cars_list.insert(5, "Rover Discovery")
print(cars_list)

cars_list.extend(["Suzuki Alto", "Daihatsu Coppen"])
print(cars_list)

cars_list2 = ["Bugatti Veyron", "Koenigesegg Agera R", "Henessey Venom GT"]

complite_cars_list = cars_list + cars_list2
print(complite_cars_list)

print(complite_cars_list.index("Honda Civic"))
index_num = complite_cars_list.index("GM Buick")
print(index_num)

complite_cars_list += ["Chervolet Cruez", "Chervolet Malibu"]
print(complite_cars_list)

complite_cars_list.reverse()
print(complite_cars_list)

complite_cars_list.pop()
print(complite_cars_list)

complite_cars_list.append("Nissan Altima")
print(complite_cars_list)

print(complite_cars_list.count("Honda Civic"))
complite_cars_list.append("Nissan Altima")
print(complite_cars_list)