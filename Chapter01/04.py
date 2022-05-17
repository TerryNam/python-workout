def hex_output():
    n_num = 0
    h_num = input('Enter a hex number:')

    for index, one_letter in enumerate(reversed(h_num)):
        n_num += int(one_letter)*(16**index)
    return n_num

print(hex_output())

