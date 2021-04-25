#!/usr/bin/env python3
from bs4 import BeautifulSoup as bs
import requests


def query():
    
    #web a acceder
    url = 'https://www.brou.com.uy/c/portal/render_portlet?p_l_id=20593&p_p_id=cotizacionfull_WAR_broutmfportlet_INSTANCE_otHfewh1klyS&p_p_lifecycle=0&p_t_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_pos=0&p_p_col_count=2&p_p_isolated=1&currentURL=%2Fcotizaciones'
    #obtenemos la estructura html
    html = requests.get(url, verify=False)
    
    #obtenemos los datos en bruto con BeautifulSoup
    req = bs(html.text, 'html.parser')
    data = dict()
    count = 1
    #Limpiamos, renombramos y transformamos
    for money in req.find_all('p', class_ = 'moneda'):
        data[str(money.text).replace('ó','o').replace('í','i')] = [str(value.text).strip().replace('.','').replace(',','.') for value in req.find_all('p', class_ = 'valor')][count*4:count*4+2]
        count += 1
    
    for key in data.keys():
        try:
            data[key] = [float(data[key][i]) for i in range(2)]
        except:
            try:
                data[key] = [float(data[key][1]),float(data[key][1])]
            except:
                continue
    
    return data

