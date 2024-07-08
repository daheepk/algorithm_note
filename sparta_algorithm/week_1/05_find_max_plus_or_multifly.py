input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    ans = 0 
    
    for number in array:
        if ans <= 1 or number <= 1:
            ans += number
        
        else : 
            ans *= number
    return ans


result = find_max_plus_or_multiply(input)
print(result)