def mysum(*items):
    if not items:
        return items
    output = items[0]
    for item in items[1:]:
        output += item
    return output

print(mysum('a,b,c,d,e'))
print(mysum(10,20,30))
print(mysum([1,2,3,4,5]))
print(mysum('a','b','c'))

