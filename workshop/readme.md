# Decoradores 
1-Pregunta teórica:

        ¿Qué es un decorador en Python y para qué se utiliza comúnmente? 

2- ✅ Mini autoevaluación 
    
    1. ¿Como se aplica a una función? 
    2. ¿Qué función interna suele tener un decorador? 

3- Código con errores para corregir
        

        def decorator(func): 
            print("Decorating...") 
            return func 

        @decorator 
        def greet(): 
            print("Hi!") 
        
        greet() 


Corregir: Mostrar cómo se aplica realmente un decorador con un wrapper. 


4- Ejercicio práctico: 

        Crea un decorador @authorize que solo permita ejecutar una función si un parámetro user tiene el atributo is_admin=True.
        Si no, debe imprimir “Acceso denegado”. Prueba el decorador con una función de ejemplo. 

5- Reflexión individual 

        ¿Qué otras funciones de Python conocés que usan decoradores? ¿Te gustaría usarlos en tus propios proyectos? 

6-  Desafío opcional 
Creá un decorador que mida el tiempo que tarda en ejecutarse una función.