#Esta función aplica cada una de las funciones que estén dentro de la lista L
# que las almacena. Aplica estas funciones con un valor de entrada para las mismas 
#de x
def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

#estas son las funciones que están dentro de la lista L
def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

applyEachTo([inc, square, halve, abs], -3)
