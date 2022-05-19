def pig_latin(word):
    p_l_word = ""
    if word[0] in 'aeiou':
        p_l_word = word + 'way'
    else:
        p_l_word = word[1::] + word[0] + 'ay'
    return p_l_word


word = input("Enter an english word: ")
p_l_word = pig_latin(word) 
print('Translated word is : ', p_l_word.lower())
