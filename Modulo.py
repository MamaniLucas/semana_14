def calcular_longitud(a):
    return len(a)


b = input ("ingrese valor: ")
print("la longitud es: ", calcular_longitud(b))

#otra forma
def calular2_longitud(texto):
    con = 0
    for i in texto:
        con += 1
    return con
