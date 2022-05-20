def pig_latin_sentence(sentence):
    pl_list = []

    for pl_words in sentence.split():
        if pl_words[0] in 'aeiou':
            pl_list.append(pl_words + 'way')
        elif pl_words[0] not in 'aeiou':
            pl_list.append(pl_words[1::] + pl_words[0] + 'ay') # append -> list method, string이 아닌 list의 변수로 받아야만 .join method를 통해서 문장으로 통합.
    return " ".join(pl_list)

if __name__ == '__main__': ## 외우고, 습관들이기!
    sentence = input('Enter a sentence: ')
    p_l_sentence = pig_latin_sentence(sentence)
    print(p_l_sentence)

    

    

