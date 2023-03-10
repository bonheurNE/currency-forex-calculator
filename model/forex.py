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
    
