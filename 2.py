# Задача 36

def print_operation_table(op, num_rows=6, num_columns=6):
    i = 2
    while i <= num_rows:
        for j in range(num_columns):
            sub_table.append(op(j+1, i))
        if i != 2: 
            for j in range(num_columns):
                sub_table.pop(0)
        main_table.append(sub_table.copy())
        i += 1
    for j in main_table: print(*j)

main_table = [(1, 2, 3, 4, 5, 6), ]
sub_table = list()
print_operation_table(lambda x, y: x * y)
