# -- Coding UTF-8 --

import sys

def valid_matrix(matrix):
    num_columns = len(matrix[0])
    for row in matrix:
        if len(row) != num_columns:
            return False
        try:
            _ = [float(element) for element in row]
        except ValueError:
            return False
    return True

def main():
    with open('terekhoff_u242_input.txt', 'r') as input_file:
        lines = input_file.readlines()
    
    matrix = []
    for line in lines:
        row = line.strip().split()
        matrix.append(row)
    
    if not valid_matrix(matrix):
        print('Ошибка: входной файл содержит неверную структуру данных.', file=sys.stderr)
        exit(1)
    
    with open('terekhoff_u242_output.txt', 'w') as output_file:
        for row in matrix:
            output_file.write(' '.join(row) + '\n')
        
    print('Успешно.')

main()
