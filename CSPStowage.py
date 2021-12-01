import sys
from constraint import *


""" 
Comprobamos el numero de parametros 
"""
if len(sys.argv) < 4:
    print("#################################\nERROR: FALTAN ARGUMENTOS\n#################################\n")

if sys.argv[1] != "CSP-tests":
    print(("#################################\nERROR: EL FICHERO QUE BUSCA SE LLAMA/DEBERIA DE LLAMARSE: CSP-tests\n#################################\n"))

""" ----- CARGAMOS EL MAPA Y GUARDAMOS LAS POSICIONES  ----- """

mapa = open("./"+sys.argv[1]+"/"+sys.argv[2])

mapa_posiciones = []

# Convertimos el mapa en matriz mediante un lista de listas
for i in mapa.readlines():
    i = list(i)
    mapa_posiciones.append(i)

# Eliminamos espacios y tabulaciones
for k in mapa_posiciones:
    for j in k:
        if (j == " ") or (j == "\n"):
            k.remove(j)

mapa.close()  # Cerramos el fichero una vez cargados los datos

""" ----- CARGAMOS LOS CONTENEDORES Y LOS IDENTIFICAMOS ----- """

contenedores = open("./" + sys.argv[1] + "/" + sys.argv[3])

contenedores_totales = []  # Lista con la informacion de cada contenedor

# AGRUPAMOS TODOS LOS CONTENEDORES
for i in contenedores.readlines():
    i = list(i)
    contenedores_totales.append(i)

# Eliminamos espacios y tabulaciones
for k in contenedores_totales:
    for j in k:
        if (j == " ") or (j == "\n"):
            k.remove(j)

contenedores.close()  # Cerramos el fichero una vez cargados los datos

"""
Verificamos que las letras del mapa son validas
"""

for i in mapa_posiciones:
    for j in i:
        if j == "N":
            pass
        elif j == "E":
            pass
        elif j == "X":
            pass
        else:
            print("#################################\nERROR: ALGUNA LETRA DEL MAPA ES ERRONEA\n#################################\n")



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CONJUNTOS DEL MAPA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""" ----- CONJUNTO DE POSICIONES DE CELDAS NORMALES (N) ----- """
posiciones_N = []
fila = 0
for i in mapa_posiciones:
    columna = 0
    for k in i:
        if k == "N":
            posiciones_N.append((columna, fila))
        columna += 1
    columna = 0
    fila += 1

""" ----- CONJUNTO DE POSICIONES DE CELDAS ESPECIALES (E) ----- """
posiciones_E = []
fila = 0
for i in mapa_posiciones:
    columna = 0
    for k in i:
        if k == "E":
            posiciones_E.append((columna, fila))
        columna += 1
    columna = 0
    fila += 1

""" ----- CONJUNTO DE POSICIONES DE CELDAS NO USABLES (X) ----- """
posiciones_X = []
fila = 0
for i in mapa_posiciones:
    columna = 0
    for k in i:
        if k == "X":
            posiciones_X.append((columna, fila))
        columna += 1
    columna = 0
    fila += 1


""" ----- CREAMOS LISTA DE POSICIONES DEL MAPA ----- """

huecos = []
for i in range(len(mapa_posiciones)):
    huecos.append(list(""))
    for k in mapa_posiciones[i]:
        huecos[i].append("")



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CONJUNTOS DE LOS CONTENEDORES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""" ----- CONJUNTO DE CONTENEDORES SEGUN EL PUERTO ----- """
contenedores_puerto_1 = []
contenedores_puerto_2 = []

for i in range(len(contenedores_totales)):
    if contenedores_totales[i][2] == "1":
        contenedores_puerto_1.append(contenedores_totales[i][0])
    elif contenedores_totales[i][2] == "2":
        contenedores_puerto_2.append(contenedores_totales[i][0])

""" ----- CONJUNTO DE CONTENEDORES SEGUN EL TIPO ----- """
contenedores_S = []
contenedores_R = []

for i in range(len(contenedores_totales)):
    if contenedores_totales[i][1] == "S":
        contenedores_S.append(str(contenedores_totales[i][0]))
    elif contenedores_totales[i][1] == "R":
        contenedores_R.append(str(contenedores_totales[i][0]))
    else:  # Comprobamos que todas las letras de los contenedores son correctas
        print(
            "#################################\nERROR: ALGUNA LETRA DE LOS CONTENEDORES ES ERRONEA\n#################################\n")




# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& COMENZAMOS EL PROBLEMA &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

problem = Problem()

"""----- CREACION DE VARIABLES Y DOMINIOS -----"""

for i in range(len(contenedores_totales)):
    if contenedores_totales[i][1] == "S":
        problem.addVariable(str(i+1), posiciones_N + posiciones_E)
    elif contenedores_totales[i][1] == "R":
        problem.addVariable(str(i+1), posiciones_E)

"""----- CREACION DE RESTRICCIONES -----"""

#PONER PRIMERO CONTENEDORES DE PUERTO 2

#RELLENAR POSICIONES POR NIVELES DE HUECOS

"""----- RECUPERACION DE SOLUCIONES -----"""

solutions = problem.getSolutions()

# UNA VEZ ACABADO TODO, QUITARLO DE LA TERMINAL, QUE SALGA UN MENSAJE ESTILO: CREADO EL FICHERO CON LOS RESULTADOS .... O ALGO ASI
print("Numero de soluciones: {0}".format(len(solutions)))
for isolution in solutions:
    print(isolution)

""" --- CREAMOS ARCHIVO TXT CON LOS RESULTADOS --- """
"""
file = open("./CSP-tests/" + sys.argv[2]+"-"+sys.argv[3]+".output", "w")
file.write("Numero de soluciones: {0}".format(len(solutions))+"\n")
for isolution in solutions:
    file.write(str(isolution)+"\n")
"""

""" --- AÑADIMOS AL SCRIPT EL TEST --- """
"""
file = open("CSP-calls.sh")
file.write()
"""