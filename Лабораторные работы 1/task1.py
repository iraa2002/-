numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum_of_numbers = sum(numbers[0:4]) + sum(numbers[5:])
len_of_numbers = len(numbers)
arithmetical_mean = (sum_of_numbers/len_of_numbers)
numbers[4] = arithmetical_mean
print("Измененный список:", numbers)
