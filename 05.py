def pig_latin():
    word = input("Enter an english word: ")

    if word[0] in 'aeiou':
        e_word = word + 'way'
        print('Translated word is : ', e_word.lower())
    elif word[0] not in 'aeiou':
        p_l_word = word[1::] + word[0] + 'ay'
        print('Translated word is : ', p_l_word.lower())

pig_latin() 
             

