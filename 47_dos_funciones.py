def F1(var1, var2):
    var1 = var1+var2
    return (F2(var1))

def F2(aux):
    aux = aux*2
    return (aux)

var1 = 10
var2 = 5
var2 = F1(var1, var2)

print("var1 es ", var1)
print("var2 es ", var2)
