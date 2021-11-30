"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

sys.setrecursionlimit(1000000000)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar puntos de interconexión aérea")
    print("3- Encontrar clústeres de tráfico aéreo")
    print("4- Encontrar la ruta más corta entre ciudades")
    print("5- Utilizar las millas de viajero")
    print("6- Cuantificar el efecto de un aeropuerto cerrado")
    print("7- Comparar con servicio WEB externo")

catalogo = None
infoAeropuertos = 'airports_full.csv'
infoRutas = 'routes_full.csv'
infoCiudades = 'worldcities.csv'

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        
        catalogo = controller.initCatalogo()
        #controller.cargarDatos(catalogo, infoAeropuertos, infoRutas, infoCiudades)
        controller.cargarDatos1(catalogo, infoAeropuertos, infoRutas, infoCiudades)
        
        print('Total aeropuertos digrafo: ', controller.numVertices(catalogo['vuelos']))
        print('Total aeropuertos grafo no dirigido: ', controller.numVertices(catalogo['vuelosIdaVuelta']))
        print('Total rutas digrafo: ', controller.numArcos(catalogo['vuelos']))
        print('Total rutas grafo no dirigido: ', controller.numArcos(catalogo['vuelosIdaVuelta']))
        print('Total de ciudades: ', controller.sizeMap(catalogo['ciudades']))


    elif int(inputs[0]) == 2:
        
        listaInterconectadosDirigido = controller.aeropuertosInterconectados(catalogo['vuelos'], catalogo)
        listaInterconectadosNODirigido = controller.aeropuertosInterconectados(catalogo['vuelosIdaVuelta'], catalogo)
        
        print('Los aeropuertos más interconectados en el digrafo son: ')
        print('')
        print('    IATA    |    Nombre    |    Ciudad    |    País')
        print('')
        
        for aeropuerto in lt.iterator(listaInterconectadosDirigido[0]):
             
            print('    {}    {}    {}    {}  '.format(aeropuerto['IATA'], aeropuerto['nombre'], aeropuerto['ciudad'], aeropuerto['pais']))
            
        print('')
        print('El número mayor de interconexiones es: ', listaInterconectadosDirigido[1])
            
        
        print('')
        print('')    
        print('Los aeropuertos más interconectados en el grafo no dirigido son: ')
        print('')
        print('    IATA    |    Nombre    |    Ciudad    |    País')
        print('')
        
        for aeropuerto in lt.iterator(listaInterconectadosNODirigido[0]):
            
            print('  {}  {}  {}  {}  '.format(aeropuerto['IATA'], aeropuerto['nombre'], aeropuerto['ciudad'], aeropuerto['pais']))
            
        print('')
        print('El número mayor de interconexiones es: ', listaInterconectadosNODirigido[1])
        
    elif inputs[0] == 3:
        pass
    
    elif inputs[0] == 4:
        
        ciudadSalida = input('Digite la ciudad de salida: ')
        ciudadLlegada = input('Digite la ciudad de llegada: ')
        
        listaCiudadesSalida = controller.infoMap(catalogo['ciudades'], ciudadSalida)
        listaCiudadesLlegada = controller.infoMap(catalogo['ciudades'], ciudadLlegada)
        
        print('A continuación se muestran las ciudades homónimas de salida')
        print('')
        print('    Ciudad    |    País    |    Latitud    |    Longitud')
        print('')
        
        for ciudad in lt.iterator(listaCiudadesSalida):
            print('{}    {}    {}    {}'.format(ciudad['nombre'], ciudad['pais'], ciudad['latitud'], ciudad['longitud']))
            
        print('')
        posSalida = input('Digite la posición de la ciudad de salida que desea: ')
        print('')
        print('')
        
        print('A continuación se muestran las ciudades homónimas de llegada')
        print('')
        print('    Ciudad    |    País    |    Latitud    |    Longitud')
        print('')
        
        for ciudad in lt.iterator(listaCiudadesLlegada):
            print('{}    {}    {}    {}'.format(ciudad['nombre'], ciudad['pais'], ciudad['latitud'], ciudad['longitud']))
            
        print('')
        posLlegada = input('Digite la posición de la ciudad de llegada que desea: ')
        
        ciudadSalidaFinal = controller.elementoLista(listaCiudadesSalida, posSalida)
        ciudadLlegadaFinal = controller.elementoLista(listaCiudadesLlegada, posLlegada)
        coordenadasCiudadSalida = (ciudadSalidaFinal['latitud'], ciudadSalidaFinal['longitud'])
        coordenadasCiudadLlegada = (ciudadLlegadaFinal['latitud'], ciudadLlegadaFinal['longitud'])
        
        listaAeropuertosSalida = controller.primerElementoLista(listaCiudadesSalida)
        listaAeropuertosLlegada = controller.primerElementoLista(listaCiudadesLlegada)
        
        menorSalida = 10000000000
        aeropuertoMenorSalida = None
        menorLlegada = 10000000000
        aeropuertoMenorLlegada = None
        
        for aeropuerto in lt.iterator(listaAeropuertosSalida):
            
            infoAeropuerto = controller.infoMap(catalogo['aeropuertos'], aeropuerto)
            coordenadasAeropuerto = (infoAeropuerto['latitud'], infoAeropuerto['longitud'])
            
            haversine = controller.calcularHaversine(coordenadasAeropuerto, coordenadasCiudadSalida)
            
            if haversine < menorSalida:
                menorSalida = haversine
                aeropuertoMenorSalida = aeropuerto
                
        for aeropuerto in lt.iterator(listaAeropuertosLlegada):
            
            infoAeropuerto = controller.infoMap(catalogo['aeropuertos'], aeropuerto)
            coordenadasAeropuerto = (infoAeropuerto['latitud'], infoAeropuerto['longitud'])
            
            haversine = controller.calcularHaversine(coordenadasAeropuerto, coordenadasCiudadLlegada)
            
            if haversine < menorLlegada:
                menorLlegada = haversine
                aeropuertoMenorLlegada = aeropuerto
                
        grafoRutasMínimas = controller.dijsktra(catalogo['vuelos'], aeropuertoMenorSalida)

    else:
        sys.exit(0)
sys.exit(0)
