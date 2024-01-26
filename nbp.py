import sys
import os
import requests
import json
from datetime import datetime
from dateutil import parser

while True:
    def start():
        os.system('cls')

    os.system('cls')
    print('Here you will check the average exchange rate of any currency for the selected day according to NBP data.\nHere we go.')

    TABLE = 'a'
    FORMAT = '%Y-%m-%d'
    OUTPUT_FILENAME = 'currency_final.json'

    ### Checking whether the user has provided arguments or requesting them
    user_args = sys.argv [1:]
    try:
        user_currency = sys.argv[1].upper()
    except IndexError:
        user_currency = input('Please enter currency: ').upper()
    try:
        user_date = sys.argv[2].lower()
    except IndexError:
        user_date = input('Please enter date: ').lower()

    ### Formatting user arguments to API requirements
    code = user_currency
    parsed_date  = parser.parse(user_date)
    date = parsed_date.strftime(FORMAT)

    ### Generating url with user arguments
    source_url = f"https://api.nbp.pl/api/exchangerates/rates/{TABLE}/{code}/{date}/?format=json"
    new_url = source_url

    ### Get the data
    response = requests.get(new_url)

    ### Validate it
    if not response.ok:
        print ('Błąd pobierania danych.')
        sys.exit(1)

    ### Filering data and save the json file
    data = response.content
    parsed_data = json.loads(data)
    mid_value = parsed_data['rates'][0]['mid']

    with open(OUTPUT_FILENAME, 'wb') as f:
        f.write(data)

    ### Print result
    print(f'The average exchange rate of 1 {code} on {date} was {mid_value} PLN.')
    print ('Saved', OUTPUT_FILENAME)

    ### Loop choice
    choice = str(input('Do you wish to check another currency/date? Y/N:'))
    if choice.lower() != 'y':
        print('Thank you. See you...')
        sys.exit(1)
    else:
        start()
