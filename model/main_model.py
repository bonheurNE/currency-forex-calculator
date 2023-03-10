import os

from . import forex

# function to create the software folder on the Desktop

# this function must be execute when the software run
def softwareFolderCreation():
    # get the current user desktop folder path
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    
    # join the desktop folder path to our software folder
    software_folder_path = os.path.join(desktop_path, 'Currency Calculator')
    
    # create the folder if not exists
    os.makedirs(software_folder_path, exist_ok=True)
    
# function to create available contries with they currency code json file
def createAvailableCurrencyFiles(temp_dir):
    forex.get_universal_currency(temp_dir)
    
# function to get all available currencies and they countries
def getCurrenciesData(temp_dir):
    data = forex.getCurrencies(temp_dir)
    return data
