def mysum_bigger(*items):

    if not items:
        return items
    output = items[0]
    for item in items[1:]:
        if  item > items[0]: 
            output += item
    return output
        
        
print(mysum_bigger(10,5,20,30,6))

