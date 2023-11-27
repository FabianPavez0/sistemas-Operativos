'''
# Def busqueda_while (arr):

def array_nombres():
    arr = ["macia", "jose", "juan", "ernes"]
    return arr

#Main

i=0
var_a_encontrado = False
array=array_nombres()
while var_a_encontrado == False:
    if array[i] == "juan":
        var_a_encontrado = True
        print(array[i])
    i+=1
'''

# Def busquedar_for (arr, var_encontrar)

def array_nombres():
    arr = ["macia", "jose", "juan", "ernes"]
    return arr

#Main

i=0
var_encontrar = False
array=array_nombres()

for nombre_lista in array:
    if "juan" in nombre_lista:
        var_encontrar = True
        print(nombre_lista)
i+=1


# Def recorrido_while (arr):
