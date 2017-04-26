import requests
from random import getrandbits
from time import sleep
from bs4 import BeautifulSoup

main_url = 'https://www.vooberlin.com/raffle'
form_url = 'https://www.vooberlin.com/raffle/index/post'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

session = requests.Session()
session.headers.update(headers)

# CHANGE the fields as the comments say
def main(limit):
    sitekey = sitekey_search()
    
    api_key = '' # COPY YOUR 2CAPTCHA KEY HERE.
    
    for i in range(1, limit):
        cap_id = session.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(api_key, sitekey, main_url)).text.split('|')[1]
        cap_answer = session.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(api_key, cap_id)).text
        while 'CAPCHA_NOT_READY' in cap_answer:
            print('Waiting for captcha. Sleeping!')
            sleep(3)
            cap_answer = session.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(api_key, cap_id)).text
        return_cap = cap_answer.split('|')[1]
        
        email = 'YOUR_EMAIL+{}@gmail.com'.format(getrandbits(40)) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        
        payload = {
            'shoes_size':'  9½  ,  43⅓  ', # put it in a format like this.
            'name' : '', # put your name
            'address' : '', # your address
            'email' : email, # don't change this
            'contact_number' : '', # put your phone number (Enter 00 before country code)
            'g-recaptcha-response' : return_cap
        }
        resp = requests.post(form_url, data=payload, headers=headers)
        print('{}/{} registered.'.format(i, limit))

# grabs sitekey
def sitekey_search():
    response = session.get(main_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    sitekey = soup.find("div", {"class":"g-recaptcha"})["data-sitekey"]
    return (sitekey)

if __name__ == "__main__":
    main(10000)
