import sys
def foo(bar=None):
    res = -1
    try: 
        res = 1/0   
    except ZeroDivisionError:
        print("Error de tipo")
        res=-1
    return(res)


print(foo())