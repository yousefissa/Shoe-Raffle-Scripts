import requests
from random import getrandbits
url = 'https://www.ruvilla.com/raffles/yeezy/submit.php'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


# CHANGE the fields as the comments say  
def main(limit):
    for i in range(1, limit):
        email = 'your_email+{}@gmail.com'.format(getrandbits(40)) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        payload = {
            'firstname': '', # put your first name
            'lastname': '', # put your last name
            'emailaddress': email, # DO NOT CHANGE
            'emailaddressverify': email, # DO NOT CHANGE
            'birthdate': '', # PUT your birth year only, like 1995
            'mobilephone': '', # put your number without spaces, like 1234567890
            'homestreet': '', # put your homestreet and number
            'homecity': '', # put your city
            'homestate': '', # PUT YOUR STATE ABREVIATION, like IL for illinois
            'homezip': '', # put your zipcode 
            'gender': 'male', # just leave this alone b.
            'shoesize': '' # put ONE shoe size, like 10, 9.5, etc.
        }
        resp = requests.post(url, data=payload, headers=headers)
        print('{}/{} registered.'.format(i, limit))

if __name__ == "__main__":
    main(10000)
