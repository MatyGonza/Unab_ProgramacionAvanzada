""" 
Ejercicio 1:
a) Rehaga al menos 3 clases con el constructor type
b) ¿Cómo se deben definir los métodos con el constructor type?
"""
new_class = type('myClass',(object, ),{'a' : True})

#se crea la funcion __init__ x fuera 
def persona_init(self,nombre):
    self.nombre = nombre
    
def estudiante_init(self,nombre,grado):
    super(Estudiante,self).__init__(nombre)
    self.grado = grado
Persona = type('Persona',(),dict(__init___=persona_init))
Estudiante = type('Estudiante',(Persona, ),dict(__init__=estudiante_init))

#Persona = type('Persona',(),dict(__init__=lambda self, nombre:setattr(self,'nombre',nombre)))
#Estudiante = type('Estudiante',(Persona, ),dict(
#    __init__=lambda self,nombre,grado:(
#        Persona.__init__(self,nombre),
#        setattr(self,'grado',grado))))
e=Estudiante(2,2)



print(e.nombre)
print(e.grado)


def decorador(fun):
    def funcion_retorno(*args,**kwargs):
        print("inicio")
        print("fin")
        res=fun(*args, **kwargs)
        return res
    
    return funcion_retorno
@decorador
def funcion_entrada(a,b):
    print("hola mundo")
    return a+b
    
funcion_entrada(4,5)