def pl_sentence():
    e_sentence = input('Enter a sentence: ')
    pl_list = []

    for pl_words in e_sentence.split():
        if pl_words[0] in 'aeiou':
            pl_list.append(pl_words + 'way')
        elif pl_words[0] not in 'aeiou':
            pl_list = pl_words[1::] + pl_words[0] + 'ay'
    return " ".join(pl_list)

    
print(pl_sentence())
    

