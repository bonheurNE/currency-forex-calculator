import requests
from bs4 import BeautifulSoup

import json
from datetime import datetime,date
import os
import time



def get_universal_currency(temp_folder_path):
    # the link to get the data
    url = "https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/lists/list-one.xml"
    
    # get the today date to use for the file name
    today_date = datetime.now()
    data = {}
    
    response = requests.get(url)
    
    soup =  BeautifulSoup(response.content, 'xml')
    
    # get data from six-group.com data
    for country in soup.find_all("CcyNtry"):
        
        country_name = country.contents[1]
        currency_name = country.contents[3]
        
        if currency_name.contents[0] == "No universal currency":
            print("No universal currency")
            pass
        else:
            currency = country.contents[5]
            currency_number = country.contents[7]
            
            data[country_name.contents[0]] = {
                "currency_country":country_name.contents[0], # country name
                "currency_name":currency_name.contents[0],   # currency name
                "currency":currency.contents[0]              #currency abreviation
            }
        
    # crete the file path with completed name
    # get the desktop folder path
    user_desktop_path =  os.path.join(os.path.expanduser('~'),'Desktop')
    
    # create a software path formed by the desktop folder  and the software folder
    software_folder_path = os.path.join(user_desktop_path, 'Currency Calculator')
    
    # create the file path with the new name of the file
    path = f"{software_folder_path}/currencies.json"
    
    # check if the file exist or not
    if os.path.isfile(path):
        pass
    else:
        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            print("local available currencies json file created ")
        
    # create the same file for tmp file
    # create the temp json file for currencies
    temp_path = f"{temp_folder_path}/currencies.json"
    with open(temp_path, 'w') as json_tmp_file:
        json.dump(data, json_tmp_file, indent=4)
        print("temp json currencies file created")
    

def getCurrencies(temp_folder_path) -> dict:
    data = {}
    
    # initializing the json temp file path 
    temp_path = f"{temp_folder_path}/currencies.json"
    with open(temp_path, 'r') as json_file:
        data = json.load(json_file)
    
    return data

        
def getConversion(amount:int|float = 0, from_c:str="",to_c:str="") -> tuple:
    from_currency = from_c
    to_currency =  to_c
    amount = amount
    
    if to_currency and from_currency:
        url = f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={from_currency}&To={to_currency}"
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")

        rate = soup.find(
            "div", class_="unit-rates___StyledDiv-sc-1dk593y-0 dEqdnx")
        
        rates = rate.find_all("p")
        
        
        from_to_rate = rates[0]
        to_from_rate = rates[1]
        
        to_from_rate = to_from_rate.text
        from_to_rate = from_to_rate.text

        f_amount = soup.find(
            "p", class_="result__BigRate-sc-1bsijpp-1 iGrAod")
        f_amount = f_amount.text
        f_amount = f_amount.split()
        f_amount = f_amount[0]
        
        
        print(f"{from_to_rate}\n{to_from_rate}\nconverted amount : {f_amount} ")
        return (from_to_rate,to_from_rate,f_amount)
    else:
        print(f"scripts abort \n'{to_currency}' not a valid currency code") 
        return ("","","0")
        pass
        
    
