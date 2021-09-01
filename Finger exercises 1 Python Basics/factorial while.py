end = 6
result = 0
while end:
    result += end
    end -= 1
print(result)

"""
Note that while tests if a result is truthy and when end reaches zero it is 
falsy so the loop stops. 
"""