##Twitter @OfficialSleak
##SLEAKS
##Variable Proxy Tester
##Updated 14/11/2017
##main
import testModule, time
url = "http://yeezysupply.com/" #Url to test proxies on
htmlContainer = "title"#Text container I.E: title/h1/h2 etc
text = "YEEZY SUPPLY" #Partial or full text that should be in the container
with open('proxies.txt') as f:
    proxies = f.read().splitlines()
for i in proxies:
    testModule.test(htmlContainer, text, url, i)
    time.sleep(1)
