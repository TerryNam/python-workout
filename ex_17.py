numbers = [1,2,3,1,2,3,4,1]

def how_many_different_numbers(numbers):
     unique_numbers = {*numbers}
     return len(unique_numbers)
     
print(how_many_different_numbers(numbers))






# define a func how_many_different_numbers ,that takes a single list of
#  integers and returns the number of different integers it contains.
#  (중복 되는 숫자 카운트 x)
# ex) numbers = [1,2,3,1,2,3,4,1]
# print(how_many_different_numbers(numbers))
#       [1,2,3,4]
# len(how_many_different_numbers(numbers)) == 4
 