simple_list = [10, 2, 8, 9, 3, 4, 1, 5]
for number in range(len(simple_list)):
    for check in range(number + 1, len(simple_list)):
        if simple_list[number] < simple_list[check]:
            simple_list[number], simple_list[check] = simple_list[check], simple_list[number]
print(simple_list)
