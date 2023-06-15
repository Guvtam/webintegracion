from datetime import date
import requests


def fecha_actual(request):
    fecha = date.today()
    return {'fecha': fecha}




def valor_dolar(request):
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    if response.status_code == 200:
        data = response.json()
        valor_dolar = data['rates']['CLP']  
        return {'valor_dolar': valor_dolar}
    return {}





