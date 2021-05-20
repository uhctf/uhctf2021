def create_bit_matrix(filename, elements_per_row):
    # Bits will be inserted in a row wise fashion
    output_csv = ''
    with open(filename, 'r') as fp:
        element_counter = 1
        for line in fp:
            line = line.strip()
            if line == '':
                continue
            output_csv += line
            output_csv += '\n' if element_counter % elements_per_row == 0 else ', '
            element_counter += 1
    return output_csv


if __name__ == '__main__':
    input_filename = 'parsed_bits.txt'
    columns = 73
    print(create_bit_matrix(input_filename, columns))
