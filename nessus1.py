import requests
accessKey="8caddd5ad72d86c509982ca2a3229f426883386b0780c114d275fdd8d5829c97"
secretKey="a53754e51fa487075a67832f885a3953cc3854620da3b8212ab3acfcf50901c5"
xapikeys="accessKey="+accessKey+"; secretKey="+secretKey+";"
header={"X-ApiKeys":xapikeys}
url="https://127.0.0.1:8834/folders"
sonuc= requests.get(url=url,headers=header,verify=False)
for i in sonuc.json()['folders']:
	print i['name']
