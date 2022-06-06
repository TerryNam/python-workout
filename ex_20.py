from fileinput import filename


def file_count(filename):
    counts = {'characters': 0,
               'words' : 0,
               'lines' : 0}
    unique_words = set() 


    for one_line in open(filename):
        counts['lines'] += 1 
        counts['characters'] += len(one_line) #one_line ->str(type)이므로, len()활용
        counts['words'] += len(one_line.split())

        unique_words.update(one_line.split())
    counts['unique_words'] = len(unique_words)

    for key, value in counts.items():
        print(f'{key}: {value}')


if __name__ == "__main__":
    
    file_count('wcfile.txt')    