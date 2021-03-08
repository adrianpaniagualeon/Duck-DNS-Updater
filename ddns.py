import requests
import time

#####################################
#             VARIABLE              #
#####################################
TOKEN = "670cd327-08e5-43e0-9765-3696eb6ebc88"
HOST = "adrianpaniagua.duckdns.org"
#####################################



def get_ip():
	global my_ip

	my_ip = requests.get('http://icanhazip.com/').text
	my_ip = my_ip.strip()



def change_dns():
	global status
	url = "https://www.duckdns.org/update?domains="+HOST+"&token="+TOKEN+"&ip="+my_ip
	r = requests.get(url)
	status = r.text

while True:
	print ("-------------------------------------------")
	print ("WEB ["+HOST+"]")
	get_ip()
	print ("CURRENT IP ["+my_ip+"]")
	change_dns()
	print ("STATUS ["+status+"]")
	print ("WAITING 5 MINUTES BEFORE THE NEXT EXECUTION")
	print ("-------------------------------------------\n\n")
	time.sleep(300)
