import numpy as np
from collections import Counter

# Importante: verifica que tu nombre y número de matrícula esten correctos

nombre = "José de Jeús González Rodríguez"
numero_de_matricula = 171877
fecha = '2025-11-09'

def capitalizacion():
    arr=np.array([17,21,44,50,79,86,140,178,203])
    media = np.mean(arr)
    mediana = np.median(arr)

    data = Counter(arr)
    # Check if there's a mode (handle empty array or no mode case if needed)
    if data:
        moda = data.most_common(1)[0][0]
    else:
        moda = None # Or handle as appropriate for your data

    desv_est = np.std(arr)

    return (media, mediana, moda, desv_est)
  
capitalizacion()


def asistencia_dispersion():
    """
    La aistencia a los 10 últimos partidos en casa de las Águilas de Baltimore fue la siguiente:   

    [20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560]    

    Calcule el rango, la varianza y la desviación stándard para estos datos   
    Regrese una tupla con el siguiente orden, como se muestra a continuación:
    """
    arr = np.array([20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560])

    rango = np.ptp(arr) 
    varianza = np.var(arr)
    desv_est = np.std(arr)
    return (rango, varianza, desv_est)
  
asistencia_dispersion()

def histograma_np():
    """
    Nota: regrese el histograma generado con la función de numpy, no genere la gráfica
    """
    calificaciones = [7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2,
                     6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2,
                     9.3, 10.0, 8.9]
    calificaciones_np = np.array(calificaciones)
    
    hist, bin_edges = np.histogram(calificaciones_np)
    return hist, bin_edges


histogram_data, bin_edges_data = histograma_np()
print("Histogram data:", histogram_data)
print("Bin edges:", bin_edges_data)

def correlacion():
    pass


# Regresa una cadena de caracteres en cada función

def problema_especifico():
    pass

def importancia():
    pass

def objetivos():
    pass

def tipo_de_datos():
    pass
