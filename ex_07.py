def ubbi_dubbi(word):
    output = []
    
    for spells in list(word): # 문자 하나하나 쪼개서 리스트에 넣어야 하므로, slpit()이 아닌 list(str)으로
        if spells in 'aeiou':
            output.append(f'ub{spells}')
        else:
            output.append(spells)
    return ''.join(output)


if __name__ == "__main__":
    word = input('Enter a word: ')
    print(ubbi_dubbi(word))
