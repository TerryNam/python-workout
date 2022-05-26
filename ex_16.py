def dictdiff(first, second):
    output = {}
    all_keys = first.keys() | second.keys()

    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key), second.get(key)]
        elif first.keys() != second.keys():
            output[key] = []
    print(output) 

        
            
if __name__ == "__main__":
    first = {'a':1, 'b':2, 'c':4}
    second = {'a':1, 'b':4, 'c':8}
    dictdiff(first,second)

         
