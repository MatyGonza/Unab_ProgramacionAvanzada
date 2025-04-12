""" 
Ejercicio 2:
● Crear la clase Punto con dos atributos x e y (ambos numéricos), con el correspondiente
constructor que recibe ambos valores.
● Definir métodos tales como:
○ eje_x
○ eje_y
○ impresion (método que devuelve en representación de string ambos valores)
○ opuesto (método que devuelve el punto opuesto -es decir con los atributos
negativos-)
○ Cualquier otro método que considere importante

"""
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def eje_x(self):
        return self.x
    
    def eje_y(self):
        return self.y
    
    def nuevo_eje_x(self, nuevo_x):
        self.x = nuevo_x
        
    def nuevo_eje_y(self, nuevo_y):
        self.y = nuevo_y

    def impresion(self):
        return f"punto({self.x},{self.y})"
    
    def __str__(self):
        return self.impresion()
        
    def opuesto(self):
        return Punto(-self.x,-self.y)
    
#Test

punto_a = Punto(1,1)
punto_b = punto_a.opuesto()
print(punto_a)
print(punto_b)
    
''' 
    Ejercicio 3:
Define una clase Línea con dos atributos: _punto_a y _punto_b. Son dos puntos por los que
pasa la línea en un espacio de dos dimensiones.
La clase dispondrá de los siguientes métodos:
● Linea(Punto, Punto) Constructor que recibe como parámetros dos objetos de la clase
Punto, que son utilizados para inicializar los atributos.
● mueve_derecha(float) Desplaza la línea a la derecha la distancia que se indique.
● mueve_izquierda(float) Desplaza la línea a la izquierda la distancia que se indique.
● mueve_arriba(float) Desplaza la línea hacia arriba la distancia que se indique.
● mueve_abajo(float) Desplaza la línea hacia abajo la distancia que se indique.
    '''
class Linea:
    def __init__(self, punto_a, punto_b):
        self.punto_a = punto_a
        self.punto_b = punto_b
        
    def mueve_derecha(self,nuevo_valor):
        self.punto_a.x += nuevo_valor
        self.punto_b.x += nuevo_valor
    
    def mueve_izquierda(self, nuevo_valor):
        self.punto_a.x -= nuevo_valor
        self.punto_b.x -= nuevo_valor
        
    def mueve_arriba(self, nuevo_valor):
        self.punto_a.y += nuevo_valor
        self.punto_b.y += nuevo_valor
    
    def mueve_abajo(self, nuevo_valor):
        self.punto_a.y -= nuevo_valor
        self.punto_b.y -= nuevo_valor
        
    def impresion(self):
        return f"Linea({punto_a},{punto_b})"
    
    def __str__(self):
        return self.impresion()
    
linea1 = Linea(punto_a, punto_b)
linea1.mueve_abajo(2)
linea1.mueve_arriba(3)
print(linea1)


''' 
    Ejercicio 4:
Desarrolla una clase Cancion con los siguientes atributos:
● titulo: una variable String que guarda el título de la canción.
● autor: una variable String que guarda el autor de la canción.
Con los siguientes métodos:
● Cancion(String, String): constructor que recibe como parámetros el título y el autor de la
canción (por este orden).
● get_titulo(): devuelve el título de la canción.
● get_autor(): devuelve el autor de la canción.
● set_titulo(String): establece el título de la canción.
● set_autor(String): establece el autor de la canción
    '''
    
class Cancion:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def set_autor(self, nuevo_autor):
        self.autor = nuevo_autor

    def __str__(self):
        return f"Canción: {self.titulo} de {self.autor}"

cancion1 = Cancion("in the end","linkin park")
print(cancion1)
cancion1.get_autor()
cancion1.set_autor("Linkin park 2")
print(cancion1)

'''  
    Ejercicio 5:
● Crea una clase Libro que modele la información que se mantiene en una biblioteca sobre
cada libro: título, autor (usa la clase Persona), ISBN, páginas, edición, editorial , lugar
(ciudad y país) y fecha de edición (como texto). La clase debe proporcionar los siguientes
servicios: getters y setters, método para leer la información y método para mostrar la
información.
● Este último método mostrará la información del libro con este formato:
Título: Introduction to Java Programming 3a. edición
Autor: Liang, Y. Daniel
ISBN: 0-13-031997-X
Prentice-Hall, New Jersey (USA)
viernes 16 de noviembre de 2001
784 páginas

    '''
    
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

persona1 = Persona("matias","gonzalez")
print(persona1)
class Libro:
    def __init__(self, titulo, autor, isbn, paginas, edicion,
                 editorial, lugar, fecha_edicion):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar
        self.fecha_edicion = fecha_edicion

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def get_autor(self):
        return self.autor

    def set_autor(self, nuevo_autor):
        self.autor = nuevo_autor

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, nuevo_isbn):
        self.isbn = nuevo_isbn

    def get_paginas(self):
        return self.paginas

    def set_paginas(self, nuevas_paginas):
        self.paginas = nuevas_paginas

    def get_edicion(self):
        return self.edicion

    def set_edicion(self, nueva_edicion):
        self.edicion = nueva_edicion

    def get_editorial(self):
        return self.editorial

    def set_editorial(self, nueva_editorial):
        self.editorial = nueva_editorial

    def get_lugar(self):
        return self.lugar

    def set_lugar(self, nuevo_lugar):
        self.lugar = nuevo_lugar

    def get_fecha_edicion(self):
        return self.fecha_edicion

    def set_fecha_edicion(self, nueva_fecha_edicion):
        self.fecha_edicion = nueva_fecha_edicion

    def mostrar_informacion(self):
        return f"""
    Título: {self.titulo}
    Autor: {self.autor}
    ISBN: {self.isbn}
    {self.editorial}, {self.lugar}
    {self.fecha_edicion}
    {self.paginas} páginas
    """
    def __str__(self):
        return self.mostrar_informacion()
    
libro1 = Libro("narnia",persona1,1234,22,"India","Indiana","Buenos Aires","21 de marzo 2025")
print(libro1)
libro1.set_autor("mas")
print(libro1)