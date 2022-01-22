#Ejercicios realizados por Belén Reynaldos García y Francisco Mellado Martínez 
#Ejercicio 1, CalculaDX
from itertools import *
def CalculaDX(posCortes):   
        """
        (list)-> list
        Calcula la longitud de las secuencias de restricción generadas por unas enzimas de restricción en una secuencia, a partir de una lista con sus puntos de corte.
            Entrada: Una lista con todas las posiciones de los puntos de corte, incluida la posición 0 y final.
            Salida: Una lista con las longitudes posibles de corte de los fragmentos de restricción.
        >>> posCortes=[0, 6, 7, 8, 9, 11, 12]
        >>> CalculaDX(posCortes)
        [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 11, 12]
        """
        # Comprobación de errores
        if type(posCortes)  not in (list,tuple):
            raise TypeError('cortes debe ser una lista')
        if not all(isinstance(i, int) for i in posCortes):
            raise TypeError('Todos los elementos de cortes deben ser números enteros')
        if len(posCortes)<2:
            raise IndexError('cortes debe ser una lista con al menos 2 elementos')
        if not all((i)>=0 for i in posCortes):
            raise AssertionError('Los números que representan las posiciones de corte no pueden ser negativos')

        # Algoritmo
        
        DistanciaX=[] 
        for i in combinations(posCortes,2): 
            DistanciaX.append(i[1]-i[0])            
        return sorted (DistanciaX)                  




#Ejercicio 2, MapaRestriccionesBusquedaExhaustivaMax
def MapaRestriccionesBusquedaExhaustivaMax(n, L):
        """
        (list)-> list
        Reconstruye los puntos de corte que son posibles soluciones a partir de las secuencias generadas tras el corte.
        Entrada: Una lista de números enteros que representan las longitudes de las secuencias generadas tras el corte (L), y el número de sitios de corte (n).
        Salida: Una lista con todas las soluciones que incluyan los puntos de cortes necesarios para generar esas secuencias, y otra lista donde tenemos las soluciones que más se acercan a M.
        >>> L=[1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7, 7, 7, 8, 9, 10, 11, 12]
        >>> n=7
        >>> MapaRestriccionesBusquedaExhaustivaMax(n, L)
        ([(0, 1, 2, 5, 7, 9, 12), (0, 1, 5, 7, 8, 10, 12), (0, 2, 4, 5, 7, 11, 12), (0, 3, 5, 7, 10, 11, 12)], [(0, 2, 4, 5, 7, 11, 12), (0, 3, 5, 7, 10, 11, 12)])
        """
        # Comprobación de errores
        if type(L) not in (list,tuple):
            raise TypeError('L debe ser una lista')
        if not all(isinstance(i, int) for i in L):
            raise TypeError('Todos los elementos de L deben ser números enteros')
        if not all(i>=1 for i in L):
            raise AssertionError('Los números representados en L deben ser mayores que cero')

        #Algoritmo
        solucionesTemporales=[]
        contador=0
        for combinacion in combinations(range(0,L[-1]+1),n): 
            if CalculaDX(combinacion)==L:                    
                solucionesTemporales.append(combinacion)                     
                if combinacion[-2] > contador:  
                    soluciones=[]
                    contador=combinacion[-2]
                    soluciones.append(combinacion)
                elif combinacion[-2] == contador:
                    soluciones.append(combinacion)
        return(solucionesTemporales, soluciones)




#Ejercicio 3, OrdenacionInversionSimple

def PermutacionDerecha(permutaInicial):
        """
        (list)->(list)
        Esta función devuelve una lista con las permutaciones que se han de realizar para ordenar dicha lista.
            Entrada: una lista de enteros que está desordenada.
            Salida: una lista con las permutaciones que se han realizado (posiciones inicial y final) para alcanzar la lista ordenada
        >>> permutaInicial=[3, 4, 2, 1, 5, 6, 7, 10, 9, 8] 
        >>> PermutacionDerecha(permutaInicial)
        [(0, 3), (2, 3), (7, 9)]
        """
        
        #Algoritmo
        permutaFinal=sorted(permutaInicial)   
        solutions = [] 

                             
        for i in range(len(permutaInicial)):   
            if i != len(permutaInicial)-1:        
                if permutaInicial[i]!=permutaFinal[i]:    
                    primera = i                             
                    segunda = permutaInicial.index(i + 1)   
                    permutaInicial[primera:segunda+1] = reversed(permutaInicial[primera:segunda+1]) 
                    solutions.append((primera, segunda)) 

                    if permutaInicial != permutaFinal:  
                        continue

        return solutions


    
def PermutacionIzquierda(permutaInicial):
        """
        (list)->(list)
        Esta función devuelve una lista con las permutaciones que se han de realizar para ordenar dicha lista, pero empezando por el lado contrario
            Entrada: una lista de enteros que está desordenada.
            Salida: una lista con las permutaciones que se han realizado (posiciones inicial y final) para alcanzar la lista ordenada
        >>> permutaInicial=[3, 4, 2, 1, 5, 6, 7, 10, 9, 8] 
        >>> PermutacionIzquierda(permutaInicial)
        [(7, 9), (1, 3), (0, 2), (0, 1)]
        """
        
        
        # Algoritmo
        permutaIzquierda=permutaInicial
        permutaFinal=sorted(permutaIzquierda)
        
        solutions= []

         
        for i in range(len(permutaInicial)-1,0,-1):   
                valorI = permutaIzquierda[i]
                
                if valorI != permutaFinal[i]:
                    segunda= i                            
                    primera = permutaIzquierda.index(i + 1)   
                    permutaIzquierda[primera:segunda+1] = reversed(permutaIzquierda[primera:segunda+1]) 
                    solutions.append((primera, segunda))
                    
                    if permutaInicial != permutaFinal:
                        continue
                                                                      
                    
                
        return solutions



def OrdenacionInversionSimple(permutaInicial):
        """
        (list)->(list)
        Esta función devuelve una lista con la lista óptima (la que tiene menos cambios) dentro de las dos otras funciones que hemos elaborado.
            Entrada: una lista de enteros que está desordenada.
            Salida: que función ofrece la lista óptima y la lista en particular
        >>> permutaInicial=[3, 4, 2, 1, 5, 6, 7, 10, 9, 8] 
        >>> OrdenacionInversionSimple(permutaInicial)
        Permutaciones derecha: [(0, 3), (2, 3), (7, 9)]
        Permutaciones izquierda: [(7, 9), (1, 3), (0, 2), (0, 1)]
        ([(0, 3), (2, 3), (7, 9)], 'PermutacionDerecha es la óptima')
        """

        # Comprobación de errores
        if type(permutaInicial) not in (list,tuple):
            raise TypeError('permutaInicial debe ser una lista')
        if not all(isinstance(numero, int) for numero in permutaInicial):
            raise TypeError('Todos los elementos de permutaInicial deben ser números enteros')
        if not all(numero>=1 for numero in permutaInicial):
            raise ValueError('Los números representados en permutaInicial deben ser mayores que cero')


        #Algoritmo
        
        permuta2=tuple(permutaInicial)
        permuta_derecha=PermutacionDerecha(permutaInicial)
        print(f"Permutaciones derecha: {permuta_derecha}")

        permutaInicial=list(permuta2)    
        permuta_izquierda=PermutacionIzquierda(permutaInicial) 
        print(f"Permutaciones izquierda: {permuta_izquierda}")

        if len(permuta_derecha) <= len(permuta_izquierda):
                return permuta_derecha, "PermutacionDerecha es la óptima"
        else:
                return permuta_izquierda, "PermutacionIzquierda es la óptima"
            

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)