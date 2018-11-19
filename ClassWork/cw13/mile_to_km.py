# variant with map

# def miles_to_km(numb_miles):
#     return numb_miles*1.6
# list_miles = [1.0, 2.0, 1.4, 2.5]
# list_km = list(map(miles_to_km, list_miles))
# print(list_km)


# variant with lambda

list_miles = [1.0, 2.0, 1.4, 2.5]
list_km = list(map(lambda x: x*1.6, list_miles))
print(list_km)

