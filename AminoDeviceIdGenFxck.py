import pyfiglet
from config import device_Id_generator_func as AminoLab
from threading import Thread
from colored import fore, back, style, attr
attr(0)
print(fore.DEEP_SKY_BLUE_1 + style.BOLD)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
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
		device_Id = authorization["result"]["url"].split("=")[4]
		print(f"device_Id: {device_Id}")
		device_Ids = open("deviceids.txt", "a+")
		device_Ids.write(f"{device_Id}\n")
	except:
		return

for r in range(threads_count):
	while True:
		Thread(target=device_Id_generator).start()
