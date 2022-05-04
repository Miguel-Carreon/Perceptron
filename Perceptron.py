import random
import time

fh = open('clean_dataset.txt')
epocas = 10000
datos_de_entrenamiento = []
datos_de_prueba = []
entradas = []
pesos = []
errores = 0
coeficiente_de_aprendizaje = 0.001

def pesos_gen():
    for i in range(3):
        sym = random.randint(0,1)
        randfloat = round(random.random() * 1, 1)
        if sym == 0:
            randfloat = randfloat*-1
        pesos.append(randfloat)

def sumatoria():
    suma_de_pesos = 0
    for x,w in zip(entradas, pesos):
        producto = (x/1000)*w #Se dividió la entrada sobre 1000
        suma_de_pesos += producto
    return suma_de_pesos

def activacion(suma_de_pesos):
    if suma_de_pesos > 0:
        return 1
    else:
        return -1

def entrenamiento(y_salida):
    for x,w in zip(entradas, pesos):
        ind = pesos.index(w)
        w_prima = w + (x/1000)*y_salida #Se realizó el cambio en la funcion de entrenamiento, ademas de que se dividió la entrada sobre 1000
        pesos[ind] =  w_prima

def file_handle():
    i = 0
    for linea in fh:
        if i < 821:
            linea = linea.strip()
            datos_de_entrenamiento.append(linea.split(","))
        else:
            linea = linea.strip()
            datos_de_prueba.append(linea.split(","))
        i += 1

start = time.time()

file_handle()
pesos_gen()
print(F'Pesos iniciales: {pesos}')

for epoca in range(epocas):
    for dato in datos_de_entrenamiento:
        entradas = []
        entradas.append(1000)
        entradas.append(int(dato[0]))
        entradas.append(int(dato[1]))

        suma_de_pesos = sumatoria()
        act = activacion(suma_de_pesos)
        
        if act != int(dato[2]):
            entrenamiento(int(dato[2]))

print(F'Pesos finales: {pesos}')

for d_prueba in datos_de_prueba:
    entradas = []
    entradas.append(1)
    entradas.append(int(d_prueba[0]))
    entradas.append(int(d_prueba[1]))
    
    suma_de_pesos = sumatoria()
    act = activacion(suma_de_pesos)

    if act != int(d_prueba[2]):
        errores += 1


print(F'Cantidad de errores: {errores}')
exito = ((len(datos_de_prueba) - errores)/len(datos_de_prueba))
print(F'Porcentaje de éxito: {exito*100}%')

end = time.time()
print(F'Tiempo: {end - start}s')