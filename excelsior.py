import requests
from random import getrandbits
url = 'https://www.excelsiormilano.com/module/antcontactcustom/sendmail'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


# CHANGE THESE VALUES
def main(limit):
    for i in range(1, limit):
        email = 'youremail+{}@gmail.com'.format(getrandbits(40)) # put your email in for your email
        payload = {
            'first_name': '', # put your first name
            'last_name': '', # put your last name
            'birth': '', # put your birthday in this exact format: 1990-01-25
            'mail': email, # dont' change this
            'number': '', # put your number without spaces, like 1234567890
            'size': '9 1/2', # put ONE shoe size, like 10, 9 1/2, etc.
            'country': 'United States',
            'state': '', # put your state
            'city': '', # put your city
            'zip': '', # put your zip code
            'street': '', # put your street here
        }
        resp = requests.post(url, data=payload, headers=headers)
        print('{}/{} registered.'.format(i, limit))

if __name__ == "__main__":
    main(10000)
