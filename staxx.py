import requests
import json
url="https://10.10.10.40:8080/login_request"
data={"username":"admin","password":"changeme"}
header={"Content-Type": "application/json"}
sonuc=requests.post(url=url,headers=header,data=json.dumps(data),verify=False)
cookie =  sonuc.headers['Set-Cookie']
cookies= cookie.split(";")[0]
url="https://10.10.10.40:8080/search/result/"
header={"Content-Type": "application/json","Cookie":cookies}
data={"searchstr":"","severity":["very-high"],"confidence":50,"interval":"7d","tlp":[],"source":[],"itype":[]} 
sonuc=requests.post(url=url,headers=header,data=json.dumps(data),verify=False)
for ioc in  sonuc.json()['data']:
	print ioc['indicator']
	print ioc['severity']
	print ioc['feed_name']
	print "="*30
