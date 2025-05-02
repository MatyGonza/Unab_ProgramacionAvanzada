"""
Respuesta 1. 
Un decorador en python es una funcion que recibe como parametro otra funcion, esto permite agregar otra funcionalidad a la funcion que recibe como parametro.

Respuesta 2.

El decorador, se aplica a una funcion mediante @nombre_funcion_decorador, sobre la funcion a decorar.

La funcion interna que tiene el decorador es wrapper (envoltorio) que es una funcion donde se agrega la funcionalidad a la funcion que se pasa como parametro puede ejecutar codigo antes o despues de la funcion que se pasa como parametro.


ej:

def decorardor(fun):
    def wrapper(*ars,**kwargs):
        return fun()
    return wrapper
return decorador

@nombre_funcion_decorador
def funcion_a_decorar():
    print "hola mundo"
    
funcion_a_decorar()



"""

#ejercicio 2 ejemplo:

def decorardor(fun):
    def wrapper(*ars,**kwargs): #funcion de envoltorio
        print("Agregando funcionalidad") #agregado de funcionalidad 
        return fun() #ejecucion de la funcion original
    return wrapper

@decorardor #Uso del decorador 
def funcion_a_decorar(): #funcion que se utiliza como parametro del decorador
    print ("hola mundo")

funcion_a_decorar() #llamada a la funcion

#ejercicio 3
""" Corregir: 

def decorator(func): 
        print("Decorating...") 
        return func 

    @decorator 
    def greet(): 
        print("Hi!") 
    
    greet() 
"""
#Ejercicio 3 corregido
def decorator(func):
    def wrapper(*args,**kwargs):    #se le agrego la funcion wrapper
        print("Decorating...")
        return func()
    return wrapper

@decorator
def greet():
    print('hi')
    
greet()

#Ejercicio 4
""" 
    Crea un decorador @authorize que solo permita ejecutar una función si un parámetro user tiene el atributo is_admin=True.
    Si no, debe imprimir “Acceso denegado”. Prueba el decorador con una función de ejemplo.
"""

def authorize(fun):
    def wrapper(usuario,*args,**kwargs):
        if not usuario.get('is_admin',False): #si no existe se considera falso, se evita si un usuario no tiene atributo is_admin pueda acceder
            print(f'El usuario {usuario.get("nombre")} No puede imprimir mensaje no es administrador')
            return
        
        print("usted es administrador accediendo al mensaje")
        return fun(usuario,*args,**kwargs)            
        
    return wrapper

@authorize
def imprimir(usuario):
    print("Hola")

usuario = dict(nombre='jorge')
usuario_admin = dict(is_admin=True,nombre='Lucas')
usuario_no_admin = dict(is_admin=False,nombre='Lola')

imprimir(usuario_admin)
imprimir(usuario_no_admin)
imprimir(usuario)

""" 
Ejercicio 5 :
Investigando, esta el decorador @Property que modifica un metodo de una clase para que sea un atributo o una propiedad.
Si me gustaria poder usarlo para poder adquirir los conocimentos
"""

""" 
6- Desafío opcional Creá un decorador que mida el tiempo que tarda en ejecutarse una función.
"""
import time

def decorador_tiempo(fun):
    def wrapper(*args,**kwargs):
        inicio=time.time()#inicio del tiempo
        resultado = fun(*args,**kwargs)
        fin=time.time()
        print(f'tiempo de ejecucion {fin - inicio:.4f}')#le resta el tiempo de inicio menos el tiempo del final
        return resultado
    return wrapper

@decorador_tiempo
def suma(a,b):
    time.sleep(1)
    return a + b

print(suma(2,2))