def firstlast(data):
    return data[:1] + data[-1:]

if __name__ == "__main__":
    print(firstlast('abcdefg'))
    print(firstlast([1,2,3,[4,5,6]]))
    print(firstlast((7,8,9,10)))
