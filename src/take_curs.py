import requests

def get_cny_exchange_rate():
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)
    
    if response.status_code == 200:
        from xml.etree import ElementTree as ET
        tree = ET.fromstring(response.content)
        
        for valute in tree.findall("Valute"):
            if valute.find("CharCode").text == "CNY":
                return float(valute.find("Value").text.replace(',', '.'))
    return None
cny_rate = get_cny_exchange_rate()