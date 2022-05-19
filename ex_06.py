def pig_latin_sentence(sentence):
    print(__name__)
    pl_list = []
    for pl_words in sentence.split():
        if pl_words[0] in "aeiou":
            pl_list.append(pl_words + "way")
        else:
            pl_list.append(pl_words[1::] + pl_words[0] + "ay")
            
    return " ".join(pl_list)


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    p_l_sentence = pig_latin_sentence(sentence)
    print(p_l_sentence)

# asdf
# asdfway

# terry
# erry + t + ay
# terryay

# asdf terry
# asdfway terryay

