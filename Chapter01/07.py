def ubbi_dubbi():
    
    words = input('Enter a word: ')
    output = []
    
    for spells in words.split():
        if spells in 'aeiou':
            output.append(f'ub{words}')
        else:
             output.append(words)
    return ''.join(output)

print(ubbi_dubbi())
       