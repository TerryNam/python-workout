def ubbi_dubbi(word):
    output = []
    
    for spells in word.split():
        if spells in 'aeiou':
            output.append(f'ub{word}')
        else:
            output.append(word)
    return ''.join(output)


if __name__ == "__main__":
    word = input('Enter a word: ')
    print(ubbi_dubbi(word))
