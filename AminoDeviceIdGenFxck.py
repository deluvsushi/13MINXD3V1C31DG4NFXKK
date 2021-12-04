import pyfiglet
from threading import Thread
from config import device_Id_generator_func as AminoLab
from colored import fore, back, style, attr
attr(0)
print(fore.DEEP_SKY_BLUE_1 + style.BOLD)
print("""Script by deluvsushi
Github : https://github.com/deluvsushi""")
print(pyfiglet.figlet_format("aminodeviceidgenfxck", font="smslant", width=58))
r = 0    
email = input("Email >> ")
password = input("Password >> ")
threads_count = int(input("Threads Count | Min - 5 / Max - 500 >> "))

# device_Id generator
def device_Id_generator():
	global r
	r = r + 1
	try:
		authorization = AminoLab.auth(email=email, password=password)
		DEVICE_ID = authorization["result"]["url"].split("=")[4].upper()
		print(f"DEVICE_ID: {DEVICE_ID}")
		DEVICE_IDS = open("deviceids.txt", "a+")
		DEVICE_IDS.write(f"{DEVICE_ID}\n")
	except:
		return

for r in range(threads_count):
	while True:
		Thread(target=device_Id_generator).start()
