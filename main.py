from modules.minmax import find_maximum_and_minimum


data_to_process = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

assert len(data_to_process) >= 3

a, b, c = data_to_process[0], data_to_process[1], data_to_process[2]

# while len(data_to_process) >= 3:
#
#     a, b, c = data_to_process[0], data_to_process[1], data_to_process[2]
#     data_to_process = data_to_process[1:]
#     if not _check_window(a, b, c):
#         raise ValueError("Invalid data")

print("it's a fib sequence!")
print(find_maximum_and_minimum('C:\\Users\\User\\Desktop\\output.txt'))