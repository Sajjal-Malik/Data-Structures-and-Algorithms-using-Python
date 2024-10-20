# determine these two things for recursion

# base case  -- case to stop the function execution
# recursive case  -- execution at this point will be just a little less complicated than original case 


def fn(n):
    if n == 1:
        return 1
    s = n + fn(n - 1)   # 
    return n
