
from unicodedata import numeric
from math import log2


print("Ejerciccio 1")

#primer ejercicio:

def imc(masa, estatura):
  imc = masa / (estatura ** 2)
  # desde aquí hacia abajo debes modificar el programa
  # modifica la variable imc
  # recuerda que los datos están en las variables masa y estatura
  return imc


#segundo ejercicio


def velocidad(distancia, tiempo):
  resultado = "La velocidad es " + str(vel1) + " km/h o "+ str(vel2) + " m/s"

  vel1= distancia / (tiempo/3600) 
  vel2 = (distancia * 1000) / tiempo


  # desde aquí hacia abajo debes modificar el programa
  # modifica la variable resultado
  # recuerda que los datos están en las variables distancia y tiempo
  return resultado

#distancia = 0.01
#tiempo = 1

#vel1= distancia / (tiempo/3600) 
#vel2 = (distancia * 1000) / tiempo

#resultado = "La velocidad es " + str(vel1) + " km/h o "+ str(vel2) + " m/s"




#tercer ejercico 3

a = False
b = False

xor = (a == True and b == True) == False and (a == False and b == False) == False

def xor(a, b):
  xor = (a == True and b == True) == False and (a == False and b == False) == False
  # desde aquí hacia abajo debes modificar el programa
  # modifica la variable xor
  # recuerda que los datos están en las variables a y b
  return xor



#EJERCICIO

lat = -33.499188
lon = -70.615126

lat_domicilio = lat
lon_domicilio = lon
estoy_al_sur = lat_domicilio - lat < 0



#ejercicio lunes 4

def sueldo(cargo):
  dinero = 0
  if cargo== "Ejecutivo":
    dinero = 90
  elif cargo == "Jefe":
    dinero = 100
  elif cargo == "Externo":
    dinero = 50
  else:
    dinero = 0
  # aquí debes implementar tu código
  # modificando la variable dinero 
  # (no modifiques nada de las lineas anteriores)
  return dinero

#ejercicio 2


def exponenciacion(numero):
  resultado = numero

  if(numero % 2 == 0):
    resultado = numero ** 3
  else:
    resultado = numero ** 2

  # aquí debes implementar tu código
  # modificando la variable resultado
  # (no modifiques nada de las lineas anteriores)
  return resultado


#ejercicio 1

def mcd(n1, n2):
  resultado=0
  while(n2 != 0):
    resultado = n2
    n2 = n1 % n2
    n1 = resultado
  return resultado


#ejercicio 2
def exponente(n):
  resultado = int(log2(n))
  return resultado


def opcion_menu(N):
  opcion = int(input("Ingresa opción desde 0 a "+str(N-1)+": "))
  while opcion < 0 or opcion > N-1:
    print("Inténtalo otra vez.")
    opcion = int(input("Ingresa opción desde 0 a "+str(N-1)+": "))



def mezclador(string_a, string_b):
  primeros = string_a[0:2]
  ultimos = string_b[len(string_b)-2:len(string_b)]
  palabra_final = primeros+ultimos
  return palabra_final


def ocurrencias(string):
    unos = string.count("1")
    ceros = string.count("0")
    resultado = unos - ceros  
    return resultado


def remover_enesimo(s, n):
    letra_rv=s[n]#letra a eliminar
    new_s=s.replace(letra_rv, '')        
    return new_s


def reemplazo(string):
    mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    resultado=""
    for letra in string:
        if letra in mayusculas:
            resultado=string.replace(letra, '$')
            
    return resultado




