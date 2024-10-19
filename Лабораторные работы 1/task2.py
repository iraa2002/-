# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44
number_of_pages = 100
number_of_lines_on_one_page = 50
number_of_symbols_in_one_line = 25
bytes_for_one_symbol = 4
total_symbols = number_of_symbols_in_one_line * number_of_lines_on_one_page * number_of_pages
total_bytes = total_symbols * bytes_for_one_symbol
disk_size_in_bytes = disk_size * 1024 * 1024
number_of_books = disk_size_in_bytes / total_bytes

print("Количество книг, помещающихся на дискету:", int(number_of_books))

