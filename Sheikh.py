import requests
from random import getrandbits
from time import sleep
from bs4 import BeautifulSoup

main_url = 'http://app.bronto.com/public/webform/render_form/az29kh7x0eyaepdiyjrpwnoaucqqy/8d8606e3ebfefedc32115d645e3832e7/addcontact'
form_url = 'http://app.bronto.com/public/webform/process/'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

session = requests.Session()
session.headers.update(headers)

# CHANGE the fields as the comments say  
def send_form(limit):
    fid, sid, sitekey = sitekey_search()

    api_key = '' # COPY YOUR 2CAPTCHA KEY HERE.

    for i in range(1, limit):
        cap_id = session.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(api_key, sitekey, main_url)).text.split('|')[1]
        cap_answer = session.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(api_key, cap_id)).text
        while 'CAPCHA_NOT_READY' in cap_answer:
            print('Waiting for captcha. Sleeping!')
            sleep(10)
            cap_answer = session.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(api_key, cap_id)).text
        return_cap = cap_answer.split('|')[1]

        email = 'YOUR_EMAIL+{}@gmail.com'.format(getrandbits(40)) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        
        payload = {
            "fid": fid, # dont change
            "sid": sid, # dont change
            "delid": "", # dont change
            "subid": "", # dont change
            "td": "", # dont change
            "formtype": "addcontact", # dont change
            "90298[29288859]": "",  # PUT YOUR FIRST NAME HERE
            "90299[29288860]": "", # PUT YOUR LAST NAME HERE
            "90300": email, # dont change 
            "90301[29288866]" : "", # PUT YOUR SHOE SIZE HERE
            "90302[29289136]": "", # dont change
            "90303[29289137]": "Agree to Terms", # dont change
            "90307[899049]": "true", # dont change
            "g-recaptcha-response": return_cap # dont change
        }
        resp = requests.post(main_url, data=payload, headers=headers)
        print('{}/{} registered.'.format(i, limit))

# finds sitekey, sid, and fid
# fid and sid are found in main_url... just in case it changes, i guess?
def sitekey_search():
    response = session.get(main_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    fid, sid = soup.find("input", {"name": "fid"})['value'], soup.find("input", {'name':'sid'})['value']
    sitekey = soup.find("div", {"class":"g-recaptcha"})["data-sitekey"]
    return (fid, sid, sitekey)

if __name__ == "__main__":
    send_form(10000)
