"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from App import controller
assert config
from time import process_time

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


#accidentsfile = 'US_Accidents_Dec19.csv'
accidentsfile = 'us_accidents_small.csv'

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de accidentes")
    print("3- Conocer los accidentes en una fecha específica")
    print("4- Conocer los accidentes anteriores a una fecha")
    print("5- Conocer los accidentes en un rango de fechas")
    print("6- Conocer el estado con más accidentes")
    print("7- Conocer los accidentes en un rango de tiempo")
    print("0- Salir")
    print("*******************************************")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de crimenes ....")
        t1_start = process_time()
        controller.loadData(cont,accidentsfile)
        t1_stop = process_time()
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
        print("\nSe cargaron", controller.accidentsSize(cont), "elementos en el árbol\nCon una altura de:", controller.indexHeight(cont))
        print("Mayor:", controller.maxKey(cont), "Menor:", controller.minKey(cont))
    elif int(inputs[0]) == 3:
        in_fe = input("Ingrese la fecha que desea conocer en el formato AAAA-MM-DD: ")
        print("\nBuscando crimenes en un rango de fechas: ")
        res = controller.getAccidentsByDate(cont,in_fe)
        if res != None:
            print("En la fecha",in_fe,"ocurrieron",res[0],"accidentes.\nSeveridad 1:",res[1],"\nSeveridad 2:",res[2],"\nSeveridad 3:",res[3],"\nSeveridad 4:",res[4])
        else:
            print("Esta fecha no se encuentra en el registro")
        
    elif int(inputs[0]) == 4:
        print("\nRequerimiento No 2 del reto 3: ")
    
    elif int(inputs[0]) == 5:
        in_fe1 = input("Ingrese la fecha menor del rango en el formato AAAA-MM-DD: ")
        in_fe2 = input("Ingrese la fecha mayor del rango en el formato AAAA-MM-DD: ")
        print("\nBuscando crimenes en un rango de fechas: ")
        res = controller.getAccidentsByDateRange(cont,in_fe1,in_fe2)
        if res != None:
            print("Entre las fechas",in_fe1,"y",in_fe2,"ocurrieron",res[0],"accidentes.\nSeveridad 1:",res[1],"\nSeveridad 2:",res[2],"\nSeveridad 3:",res[3],"\nSeveridad 4:",res[4])
        else:
            print("Esta fecha no se encuentra en el registro")

    elif int(inputs[0]) == 6:
        initialDate = input("Ingrese la fecha menor del rango en el formato AAAA-MM-DD: ")
        finalDate = input("Ingrese la fecha mayor del rango en el formato AAAA-MM-DD: ")
        res = controller.getStateByDateRange(cont,initialDate,finalDate)
        if res is None:
            print("Recuerda ingresar bien las fechas de acuerdo a los datos que tenemos registrados y a las instrucciones.")
        elif res[0] is None:
            print("No hay ningún registro de accidentes en ese rango de fechas.")
        else:
            print("El estado que más se repite entre", initialDate, "y", finalDate, "es:", res[1], "y la fecha con más accidentes en ese rango fue", res[0])
    
    elif int(inputs[0]) == 7:
        print("\nRequerimiento No 5 del reto 3: ")
    
    else:
        sys.exit(0)
sys.exit(0)
