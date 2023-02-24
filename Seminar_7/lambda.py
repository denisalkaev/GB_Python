def select(f, col): # map is the same function
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1,2,4,5,6,7,8]
res = select(int, data) # format numbers to integer
print(res)
res = where(lambda x: x % 2 == 0, res) # take only even numbers
print(res)
res = [select(lambda x: x**2, res)]
print(res)