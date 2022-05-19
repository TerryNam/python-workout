def ubbi_dubbi():
    
    word = input('Enter a word: ')
    output = []
    
    for spells in word.split():
        if spells in 'aeiou':
            output.append(f'ub{word}')
        else:
             output.append(word)
    return ''.join(output)

print(ubbi_dubbi())
       