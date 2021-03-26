#!/usr/bin/env python3
import requests
import re


def query():
    #web a acceder
    url = 'https://www.brou.com.uy/c/portal/render_portlet?p_l_id=20593&p_p_id=cotizacionfull_WAR_broutmfportlet_INSTANCE_otHfewh1klyS&p_p_lifecycle=0&p_t_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_pos=0&p_p_col_count=2&p_p_isolated=1&currentURL=%2Fcotizaciones'
    #obtenemos la estructura html en formato utf-8
    req = requests.get(url, verify=False)
    #guardo como texto
    f = req.text
    #convertimos a string
    f = str(f)
    
    #obtenemos solo la tabla
    table = f.split("<table")
    table = str(table[1]).split("</table")
    table = str(table[0])
    
    #seguimos con regex
    sep = '>.*?<'
    table = re.findall(pattern=sep,string=table)

    #limpiamos los datos
    cots = ['Moneda']
    for i in range(4,len(table)):
        if table[i] not in ['><', '> <', '>&nbsp;&nbsp;<']:
            cots.append(table[i][1:-1].strip().replace('.','').replace(',','.'))

    #creamos diccionario (map)
    datos = {'Moneda':['Compra','Venta']}
    monedas = ['Dolar','Dolar eBrou','','','','','','Guarani']
    for i,j in enumerate(cots):
        if i%5 == 0:
            try:
                if i//5 in [1,2,8]:
                    j = monedas[i//5+1]
                datos[j] = [float(cots[i+1]),float(cots[i+2])]
            except:
                try:
                    datos[j] = [cots[i+1],float(cots[i+2])]
                except:
                    datos[j] = cots[i+1:i+3]
    
    return datos
