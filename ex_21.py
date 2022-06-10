from fileinput import filename
import os

def find_longest_word(filename):

    longest_word = ''
    with open(filename) as onefile:
        for one_line in onefile:
            for one_word in one_line.split():
                if len(one_word) > len(longest_word):
                    longest_word = one_word
    return longest_word

def find_all_longest_word(dirname):
    return {filename:
            find_longest_word(os.path.join(dirname,filename))
            for filename in os.listdir(dirname)
            if os.path.isfile(os.path.join(dirname,filename))}


## 동인한 길이의 단어 중복처리는 어떻게??
if __name__ == "__main__":

    print(find_all_longest_word('./test_files'))    