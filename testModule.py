##Twitter @OfficialSleak
##SLEAKS
##Variable Proxy Tester
##Updated 14/11/2017
##TESTMODULE
import requests, bs4
from bs4 import BeautifulSoup
headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
    }
def test(htmlContainer, text, url, proxy):
    print("Testing Proxy: "+proxy)
    ip,port,username,password = proxy.split(":")
    formattedProxy = (username+':'+password+'@'+ip+':'+port)
    print(formattedProxy)
    proxies = {'http': 'http://'+formattedProxy}
    proxies = {'https': 'https://'+formattedProxy}
    session = requests.Session()
    session.proxies = proxies
    try:
        resp = requests.get(url, headers=headers,proxies=proxies, timeout=10)
        container = BeautifulSoup(resp.text, "lxml").find(htmlContainer)
        if (text) in container.getText():
            print("Success!")
            file = open('working.txt', 'a')
            file.write(proxy+'\n')
            file.close()
        else:
            print("Failed")
        return
    except:
        print("Failed")
