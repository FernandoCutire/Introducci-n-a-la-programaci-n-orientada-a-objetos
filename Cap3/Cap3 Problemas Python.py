
# coding: utf-8

# # Cap3 Problemas Python

# ## Estos son problemas son del cap3 usando programación orientada a objetos

# In[8]:


import math


# ### 1.  Calcular el área de un triángulo (1/2*b*h). Imprimir los datos de entrada y el resultado.

# In[45]:


class triangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        print("Se ha creado un triangulo con base de {} y altura {}".format(base, altura))
    def calcular_area(base, altura):
        area = (1/2)*base*altura
        print(area)


# In[54]:


t = triangulo(15.,12)
t = triangulo.calcular_area(15.,12)


# ### 2. Calcular el área de un círculo dado el radio (π r) e imprimir el area

# In[75]:


class circulo():
    def __init__(self, radio=0):
        self.radio = radio
        print("Has creado un circulo de radio {}".format(radio))
    def calcular_area_circulo(self):
        area_circulo = math.pi * self.radio
        print(area_circulo)


# In[77]:


c = circulo(2)
c.calcular_area_circulo()


# ### 3. Calcular los grados Fahrenheit (F = 9/5 ( C° + 32)) dados los centígrados. Imprimir el resultado.
# 

# In[83]:


class grados_fahrenheit():
    def __init__(self, centigrados):
        self.centigrados = centigrados
    def calcular_grados_fahrenheit(self):
        grados_fahrenheit = (9/5)*(self.centigrados + 32)
        print(grados_fahrenheit)


# In[84]:


f = grados_fahrenheit(35)
f.calcular_grados_fahrenheit()


# ### 4. Calcular el salario de un empleado a partir de los siguientes datos de entrada: nombre del empleado, horas trabajadas, tarifa por hora, total de deducciones. 

# In[91]:


class empleado():
    def __init__(self, nombre=0, horas_trabajadas=0, tarifa_hora=0, deducciones=0):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora
        self.deducciones = deducciones
    def calcular_salario(self):
        print("Empleado: {}".format(self.nombre))
        print("Horas trabajadas: {}".format(self.horas_trabajadas))
        print("Tarifa por hora: {}".format(self.tarifa_hora))
        print("Deducciones: {}".format(self.deducciones))
        salario = (self.horas_trabajadas*self.tarifa_hora)-self.deducciones
        print("Tu salario es {}".format(salario))


# In[92]:


fernando = empleado("Fernando",80,100,500)
fernando.calcular_salario()


# ### 5. Calcular salario bruto = tarifa por horas * horas trabajadas y el salario neto = salario bruto– deducciones. Imprimir salario bruto y salario neto.

# In[116]:


class salario():
    def __init__(self,horas_trabajadas=0, tarifa_hora=50, deducciones = 500):
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora
        self.deducciones = deducciones
    def calcular_salario_bruto(self):
        salario_bruto = self.tarifa_hora*self.horas_trabajadas
        return salario_bruto
    def calcular_salario_neto(self):
        salario_bruto = self.tarifa_hora*self.horas_trabajadas
        salario_neto = salario_bruto - self.deducciones
        print(salario_neto)


# In[122]:


A = salario(100)
A.calcular_salario_bruto()


# In[123]:


A.calcular_salario_neto()


# ## Solución general

# In[135]:


class Promedio():
    def __init__(self,listaDeNotas):
        self.listaDeNotas = listaDeNotas
    def CalcularPromedio(self):
        sumaDeNotas = 0.0
        for nota in self.listaDeNotas:
            sumaDeNotas += nota
        prom = sumaDeNotas/len(self.listaDeNotas)
        return prom
#(n1+n2+n3...etc)/(numero de notas)
pro = Promedio([4,5])
print(pro.CalcularPromedio())


# ### 5. Leer el nombre del estudiante y tres notas, calcular e imprimir la nota promedio.

# In[132]:


class estudiante():
    def __init__(self, nota1=0, nota2=0, nota3=0):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    def calcular_nota_promedio(self):
        nota_promedio = (self.nota1+self.nota2+self.nota3)/3
        return nota_promedio


# In[133]:


Asley = estudiante(100,20,30)
Asley.calcular_nota_promedio()


# ### 6. Leer dos números, calcular e imprimir el valor de suma, resta, producto y su división.

# In[139]:


class propiedades():
    def __init__(self,numero1=0, numero2=0):
        self.numero1 = numero1
        self.numero2 = numero2
    def suma(self):
        resultado_suma = self.numero1 + self.numero2
        print(resultado_suma)
    def resta(self):
        resultado_resta = self.numero1 - self.numero2
        print(resultado_resta)
    def producto(self):
        resultado_producto = self.numero1 * self.numero2
        print(resultado_producto)
    def division(self):
        resultado_division = self.numero1/self.numero2
        print(resultado_division)
        
numeros = propiedades(1,2)
numeros.suma()
numeros.resta()
numeros.producto()
numeros.division()


# ###  7. Leer el largo, ancho y altura de una habitación. Calcular e imprimir cuántos metros cuadrados se requieren comprar de alfombra (área =largo × ancho), y cuántos metros cuadrados de papel se requieren para tapizar la pared de la habitación (P = 2 * largo * ancho * altura).

# In[1]:


class habitacion():
    def __init__(self, largo, ancho, altura):
        self.largo = largo
        self.ancho = ancho
        self.altura = altura
    def calcular_alfombra(self):
        alfombra = self.largo*self.ancho
        print(alfombra)
    def calcular_papel(self):
        papel = 2*(self.largo+self.ancho+self.altura)
        print(papel)
sala = habitacion(10,20,30)
sala.calcular_alfombra()
sala.calcular_papel()


# ### 8. Calcular e imprimir el precio de venta de un artículo. Se tienen los datos descripción del artículo y costo de producción. El precio de ventas se calcula añadiendo al costo el 12% como utilidad y el 15% de impuesto.

# In[5]:


class articulo():
    def __init__(self, descripcion, costo_produccion):
        self.descripcion = descripcion
        self.costo_produccion = costo_produccion
    def calcular_precio(self):
        utilidad = self.costo_produccion * 0.12
        impuesto = self.costo_produccion * 0.15
        precio = self.costo_produccion + utilidad + impuesto
        print("Es una {}, con un costo de {}".format(self.descripcion, precio))
naranja = articulo("naranja",20)
naranja.calcular_precio()


# ### 9. Una niña deja caer su cartera desde el último piso de la torre Sears (1,454 pies de altura). Cree un algoritmo que calcule la velocidad de impacto al llegar al suelo. Utilizar la fórmula v = √ 2gh, donde h es la altura de la torre, g es la gravedad de 32 pies/seg 2

# In[12]:


class velocidad():
    def __init__(self, altura=1454, gravedad=32):
        self.altura = altura
        self.gravedad = gravedad
    def algoritmo(self):
        velocidad = math.sqrt(2*self.gravedad*self.altura)
        print(round(velocidad,2))


# In[13]:


cartera = velocidad()
cartera.algoritmo()


# ### 10. Elabore un algoritmo que lea una cantidad de horas e imprima su equivalencia en minutos, segundos y días.

# In[14]:


class horas():
    def __init__(self, horas):
        self.horas = horas
    def calcular_equivalencias(self):
        minutos = self.horas * 60
        segundos = self.horas * 3600
        dias = self.horas/24
        print("Las {} horas insertadas son equivalentes a {} minutos {} segundos y {} dias".format(self.horas, minutos, segundos, dias))


# In[16]:


a = horas(6)
a.calcular_equivalencias()

