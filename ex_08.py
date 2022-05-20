def strsort(word):
    return ''.join(sorted(word))


if __name__ == "__main__":
    word = input('Enter a word: ')
    sorted_word = strsort(word)
    print(sorted_word)
    
