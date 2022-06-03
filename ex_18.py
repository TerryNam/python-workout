#with open('text_test.txt', 'r') as f:
#    last_line = f.readlines()[-1]
#print(last_line)

def get_final_line(filename):
    final_line = ''
    for current_line in open(filename):
        final_line = current_line
    return final_line

print(get_final_line('text_test.txt'))