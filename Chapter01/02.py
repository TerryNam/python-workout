def mysum(*numbers): # argument를 'numbers'로만 하면 안됨 
    output = 0

    for number in numbers:
        output += number
    return output

print(mysum(10,20,30,40,50))
