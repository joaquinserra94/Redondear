print(90/7)
print(round(90/7))

resultado = 80/7
redondeo = round(resultado)
print(redondeo)

valor = round(95.666666666666666, 2)
print(valor)
print(type(valor))

valor = round(95.666666666666666) #aqui si nos da un integer porque estamos modificando el numero de base
print(valor)
print(type(valor))

valor = 95.666666666666666
print(round(valor)) #aqui me devolvera un int pero me lo mostrara como float, porque el numero sigue siendo
print(type(valor))# float pero lo que modificamos es la impresion del mismo.