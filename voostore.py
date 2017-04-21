import requests
from random import getrandbits
url = 'https://www.vooberlin.com/raffle/index/post'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


# CHANGE the fields as the comments say  
def main(limit):
    for i in range(1, limit):
        email = 'your_email+{}@gmail.com'.format(getrandbits(40)) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        payload = {
			'shoes_size':'  9½  ,  43⅓  ', # put it in a format like this.
			'name' : '', # put your name
			'address' : '', # your address
			'email' : email, # don't change this
			'contact_number' : '' # put your phone number
        }
        resp = requests.post(url, data=payload, headers=headers)
        print('{}/{} registered.'.format(i, limit))

if __name__ == "__main__":
    main(10000)
