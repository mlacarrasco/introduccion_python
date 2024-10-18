import sys
def foo(bar=None):
    res= 1/0
    return(res)

try: 
    foo()
except:
    exc_type, exc_value, tb = sys.exc_info()
    print(exc_type)
 