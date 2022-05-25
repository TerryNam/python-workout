from collections import Counter


def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]

def most_repeating_word(words):
    return max(words, key = most_repeating_letter_count)


if __name__ == "__main__":
    sentence = "This is a test of the most repeating spells in a word"
    words = sentence.split()
    print(most_repeating_word(words))
    
    


  

# sentence = hello everybody welcome to the python world
# sentence의 각 단어들이 리스트(words)에 인자로 들어가야 함
# : ['hello', 'everybody', 'welcome', 'to', 'the', 'python', 'world']
# words에 대하여 Counter 메소드 실행-> .most_common(1)[0][1] -> 리스트 내의 튜플 중
# 가장 많이 반복 된 스펠의 알파벳 출력 
# most_repeating_word(words) 함수를 통해 가장 많이 반복된 스펠이 포함된 단어 출력


