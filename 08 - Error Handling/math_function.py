class math_function:
    def __init__(self, lista_numeros):
        if (type(lista_numeros) != list):
            self.lista = []
            raise ValueError('Se ha creado una lista vacía. Se esperaba una lista de números enteros')  
        else:
            self.lista = lista_numeros
        
    def verifica_primo(self):
        for e in self.lista:
            if (self.__verifica_primo(e)):
                print("El número ", e, " SI es número primo")
            else:
                print("El número ", e , " NO es número primo")

    def __verifica_primo(self, num):
        if num in [1, 2]:
            return True
        elif num < 1:
            return False
        else:
            for i in range(2, num ):
                cont = 2
                if num % i == 0:
                    cont += 1
                    break
            return cont <= 2
        
    def lis_repetidos1(self,mayor=True): # Mayor: True por mayor, False por menor.
        cont=1
        acum=0
        num_acum=0
        for i in range(0, len(self.lista)):
            for j in range(i+1, len(self.lista)):
                if self.lista[i] == self.lista[j]:
                    num=(self.lista[i])
                    cont +=1
            if cont > 1:
                if cont > acum:
                    acum = cont
                    num_acum = num
                elif cont == acum:
                    if mayor and num > num_acum or not mayor and num < num_acum:
                        num_acum = num
            cont=1
            num=""
        print ('El Valor modal es ', num_acum, ' y se repite ', acum, ' veces')
    
    def convertir_grados(self, origen, destino):
        for e in self.lista:
            print(e, ' grados', origen, ' son ', self.__conversion_grados(e, origen, destino))

    def __conversion_grados(self,valor=0, origen=0, destino=0):
        '''Función que convierte entre grados celsius, farenheit y kelvin.
            se ingresa el 'valor' a ser convertido, 
            se indica el tipo de 'origen' 0=celsius, 1= farenheit y 2=kelvin
            se indica el tipo de 'destino' 0=celsius, 1=farenheit y 2 =kelvin.
        '''
        if origen == 'Celsius':  # Celsius
            if destino== 'Celsius': # Celsius
                return(valor, "grados Celsius")
            elif destino=='Farenheit': # farenheit
                valor_c=round((valor*9/5)+32, 1)
                return(valor_c, ' grados farenheit')
            else:   # kelvin
                valor_c=round((valor+273.15), 1)
                return(valor_c, ' grados kelvin')
                
        elif origen=='Farenheit': #Farenheit
            if destino=='Celsius':   # Celsius
                valor_c=round((valor + 32)/(9/5), 1)
                return(valor_c, ' grados celsius')
            elif destino=='Farenheit': # Farenheit
                return(valor, ' grados farenheit')
            else:   # Kelvin
                valor_c =round((5/9)*valor - (160/9) + 273.15, 1)
                return(valor_c, ' grados kelvin')
        else: # kelvin
            if destino=='Celsius':   # Celsius
                valor_c = round(valor-273.15,1)
                return(valor_c, ' grados celsius')
            elif destino=='Farenheit': # Farenheit
                valor_c = round(9*(valor +(160/9) - 273.15)/5, 1)
                return(valor_c, ' grados farenheit')
            else:   # Kelvin   
                return(valor, ' grados kelvin')

    def factorial(self):
        for e in self.lista:
            print("El factorial de ", e , ' es ', self.__factorial(e))

    def __factorial(self,nro):
        if (type(nro)==int and nro>0):
            if nro > 1:
                nro = nro * self.__factorial(nro-1)
            return nro
        else:
            print('Solo se aceptan números enteros positivos mayores a 1')