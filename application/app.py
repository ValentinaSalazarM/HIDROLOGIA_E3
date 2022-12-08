import pandas as pd
def frecuencias (datos, intervalos, nivel_agregacion):
    maximo = max(datos['Caudal agregado [m³/s]'])
    minimo = min(datos['Caudal agregado [m³/s]'])
    rango = maximo - minimo
    n_intervalos = intervalos
    amplitud = rango/n_intervalos
    n_datos = datos['Caudal agregado [m³/s]'].count()
    limite_sup = [maximo]
    limite_inf = [maximo - amplitud]

    for i in range (1, n_intervalos):
        limite_sup += [limite_inf[i-1]]
        limite_inf += [limite_sup[i]-amplitud]

    frecuencias = [0]*len(limite_sup)
    frecuencias_acumuladas = [0]*len(limite_sup)
    porcentaje = [0]*len(limite_sup)

    for i in range(0, len(limite_sup)):
        for q in datos['Caudal agregado [m³/s]']:
            if (q > limite_inf[i] and q <= limite_sup[i]):
                frecuencias[i] += 1
            if (i == 0):
                frecuencias_acumuladas[i] = frecuencias[i]
            else:
                frecuencias_acumuladas[i] = frecuencias_acumuladas[i - 1] + frecuencias[i]
            porcentaje[i] = round((frecuencias_acumuladas[i]/n_datos) * 100,3)
    
    for i in range(0, len(limite_inf)):
        limite_inf[i] = round(limite_inf[i], 3)
    consolidado = pd.DataFrame()
    consolidado ["Caudal " + nivel_agregacion + " [m³/s]"] = limite_inf
    consolidado ["% Tiempo que el caudal es igualado o excedido"] = porcentaje
    return consolidado, minimo, maximo, rango, amplitud, n_datos

def grafica_tabla (estacion, nivel_agregacion, intervalos):
    
    color = "lightseagreen"
    if (estacion == "Cantarrana"):
        datosDiarios = pd.read_excel('application/Cantarrana.xlsx')
        color = "slateblue"
    else:
        datosDiarios = pd.read_excel('application/PuenteBosa.xlsx')
    columna = datosDiarios.columns[1]
    if nivel_agregacion == "Semanal":
        datosDiarios[nivel_agregacion] = datosDiarios[columna].rolling(7).mean().shift(-6)
    elif nivel_agregacion == "Decadal":
        datosDiarios[nivel_agregacion] = datosDiarios[columna].rolling(10).mean().shift(-9)
    elif nivel_agregacion == "Quincenal":
        datosDiarios[nivel_agregacion] = datosDiarios[columna].rolling(15).mean().shift(-14)
    elif nivel_agregacion == "Mensual":
        datosDiarios[nivel_agregacion] = datosDiarios[columna].rolling(30).mean().shift(-29)
    else:
        datosDiarios[nivel_agregacion] = datosDiarios[columna]
    datos = datosDiarios.dropna()
    datos = datos['Fecha']
    datos = datos.to_frame()
    datos['Caudal agregado [m³/s]'] = datosDiarios[nivel_agregacion]
    consolidado, minimo, maximo, rango, amplitud, n_datos = frecuencias(datos, intervalos, nivel_agregacion)
    consolidado.to_excel(estacion + "_" + nivel_agregacion  + ".xlsx")    
    #consolidado.plot(x = "% Tiempo que el caudal es igualado o excedido", y = "Caudal " + nivel_agregacion + " [m³/s]", color = color).get_figure().savefig(estacion + "_" + nivel_agregacion + '.jpg')
    return consolidado, minimo, maximo, rango, amplitud, n_datos