import os

os.system("apt-get insatll figlet")
os.system("apt-get insatll ncrack")
os.system("clear")
os.system("figlet Kaba Kuvvet")
print("""
 1 ) FTP	
 2 ) SSH
 3 ) TelNet		
 4 ) HTTP
 5 ) SMB
 6 ) RDP
 7 ) VNC
 8 ) SIP
 9 ) Redis
 10 ) PostgreSOL
 11 ) MySol
""")

işlem = input("İşlem Numarası Giriniz : ")
port = input("Port Giriniz : ")
ıp = input("Hedef IP Giriniz : ")
liste = input("Username Dosyası Kısa Yolu : ")
şifre = input("Wordlist Dosyası Kısa Yolu Giriniz :")

if işlem == 1 :
	os.system("ncrack -p " + port + "-U " + liste + " -P " + şifre + " " + ıp)
elif işlem == 2 :
	os.system("ncrack -p " + port + "-U " + liste + " -P " + şifre + " " + ıp)
elif işlem == 3 :
	os.system("ncrack -p " + port + "-U " + liste + " -P " + şifre + " " + ıp)
elif işlem == 4 :
	os.system("ncrack -p " + port + "-U " + liste + " -P " + şifre + " " + ıp)
elif işlem == 5 :
	os.system("ncrack -p " + port + "-U " + liste + " -P " + şifre + " " + ıp)
elif işlem == 6 :
	os.system("ncrack -p " + port + "-U " + liste + " -P " + şifre + " " + ıp)
elif işlem == 7 :
	os.system("ncrack -p " + port + "-U " + liste + " -P " + şifre + " " + ıp)
elif işlem == 8 :
	os.system("ncrack -p " + port + "-U " + liste + " -P " + şifre + " " + ıp)
elif işlem == 9 :
	os.system("ncrack -p " + port + "-U " + liste + " -P " + şifre + " " + ıp)
elif işlem == 10 :
	os.system("ncrack -p " + port + "-U " + liste + " -P " + şifre + " " + ıp)
elif işlem == 11 :
	os.system("ncrack -p " + port + "-U " + liste + " -P " + şifre + " " + ıp)
else:
	print("Hatalı Tuşlama Yaptınız!!!")
