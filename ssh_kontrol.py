import paramiko
client = paramiko.SSHClient()
#client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
dosya = open("bilgiler.txt","r")
icerik = dosya.read()
dosya.close()
for bilgi in icerik.split("\n"):
	try:
		IP=bilgi.split("-")[0]
		user=bilgi.split("-")[1]
		passwd=bilgi.split("-")[2]
		print("IP-",str(user),"-",str(passwd))
		client.connect(IP,username=user,password=passwd)
		stdin, stdout, stderr = client.exec_command('cat /etc/passwd')
		if "kaleileriteknoloji" in stdout.readlines():
			print("kaleileriteknoloji kullanıcısı var")
		else:
			print("Pentestte eklenen kullanıcı yok")
		client.close()
	except:
		pass
