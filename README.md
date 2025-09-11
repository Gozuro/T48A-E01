# T48A-E01

Instrucciones:

## 1. Importe numpy solo una vez, como se muestra a continuación:
```python
import numpy as np

# Importante: verifica que tu nombre y número de matrícula esten correctos

nombre = ""
numero_de_matricula = 000000
fecha = '2025-11-09'
```

## 2.   El 30 de junio de 1992, la capitalización de mercados de valores del Pacífico y Asia fue:   

País |  Capitalización (en miles de millones de dólares)
-----|---------------------------------------------------
Filipinas | 17
Indonesia | 21
Tailandia | 44
Singapur | 50
Malasia | 79
Corea del Sur | 86
Taiwan | 140
Hong Kong | 178
Australia | 203

a) Encuentre la media aritmética de los datos   
b) Encuentre la mediana de los datos   
c) Encuentre la moda de los datos   
e) Encuentre la desviación estándar de los datos   

regrese una tupla en el siguiente orden, como se muestra abajo:   

```python
def capitalizacion():
    # inserta tu código aquí
    return (media, mediana, moda, desv_est)
```

## 3. Utiliza los datos proporcionados para calcular lo que se te solicita en el docstring

```python

def asistencia_dispersion():
    """
    La aistencia a los 10 últimos partidos en casa de las Águilas de Baltimore fue la siguiente:   

    [20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560]    

    Calcule el rango, la varianza y la desviación stándard para estos datos   
    Regrese una tupla con el siguiente orden, como se muestra a continuación:
    """
    # inserta tu código aquí
    return (rango, varianza, desv_est)
```

## 4.    Genere un histograma de las siguientes calificaciones en el examen parcial:


```python
def histograma_np():
    """
    Nota: regrese el histograma generado con la función de numpy, no genere la gráfica
    """
    calificaciones = [7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2,
                     6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2,
                     9.3, 10.0, 8.9]
    pass
```

## 5.    Analiza la correlación entre los datos de Tamaño y Precio y Regresa el coeficiente de Pearson


   Tamaño (m²) | Precio (MXN)
   ------------|------------
          100  |    1305710
          120  |    1658277
          140  |    1894167
          160  |    2136552
          180  |    2298267
          200  |    2553624
          220  |    2780503
          240  |    3289726
          260  |    3472743
          280  |    3779477

```python
def correlacion():
    pass
```



La **probabilidad condicional** es un concepto fundamental en estadística que permite calcular la probabilidad de que ocurra un evento A, dado que ya ha ocurrido otro evento B. Es especialmente útil cuando los eventos no son independientes y el conocimiento de uno afecta la probabilidad del otro.

## 📘 ¿Qué es la probabilidad condicional?
Se representa como **P(A|B)** y se lee como “la probabilidad de A dado B”. Esta fórmula indica cuánto cambia la probabilidad de A cuando sabemos que B ha ocurrido.

- Ejemplo cotidiano: Supón que en una escuela, el 80% de los estudiantes practican fútbol y el 35% practican tanto fútbol como baloncesto.
  Si eliges al azar a un estudiante que practica fútbol, ¿cuál es la probabilidad de que también practique baloncesto? Usamos la fórmula:

$$ 𝑃(Baloncesto∣Fútbol)=𝑃(Baloncesto ∩ Fútbol) / 𝑃(Fútbol) $$
Es decir, hay un 43.75% de probabilidad de que ese estudiante también juegue baloncesto

## 6.        Resuelve el siguiente ejercicio de probabilidad condicional

La tienda de departamentos Friendly ha sido objeto de muchos robos durante el último mes; pero debido al aumento a las medidas de seguridad, se han detenido 250 ladrones. Se registró el sexo de cada ladrón; también se anotó si se trataba de un primer delito o era reincidente. Los datos se resumen en la siguiente tabla.

Sexo | Primera ofensa | Reincidente
-----|----------------|------------
Hombre | 60 | 70
Mujer | 44 | 76

Suponga que se selecciona al azar un ladrón detenido, calcule
* la probabilidad de que el ladrón sea hombre: p_hombre
* la probabilidad de que sea la primera ofensa, dado que es hombre: p_po_hombre

Regrese ambos datos en una tupla con el siguiente orden
(p_hombre, p_po_hombre)

```python
def probabilidad_condicional():
    # inserta tu código aquí
    return (p_hombre, p_po_hombre)
```

"""Contesta las siguientes preguntas

Definición del Problema:

## 7.     ¿Cuál es el problema específico que se desea resolver con la minería de datos?
## 8.     ¿Por qué es importante resolver este problema?

Objetivos del Proyecto:

## 9.     ¿Cuáles son los objetivos principales del anteproyecto?
## 10.     ¿Qué resultados esperas obtener al final del proyecto?

Recolección de Datos:

## 11.    ¿Qué tipo de datos se necesitarán para este proyecto?

```python

# Regresa una cadena de caracteres en cada función

def problema_especifico():
    pass

def importancia():
    pass

def objetivos():
    pass

def tipo_de_datos():
    pass
```
