############################################
#  Instagram Username Availability Checker #
#  Github.com/starstrucked                 #
############################################
import requests, os
from pystyle import Colors
from threading import Thread
os.system('cls||clear')
print(f""" 
{Colors.blue}//{Colors.white} IG Username Checker 
""")
print("")
username_file = input(f"{Colors.blue}\{Colors.reset}?{Colors.blue}\{Colors.reset} Usernames File: ")
availablecount = 0
takencount = 0
errorcount = 0
def title():  
    while True:
        os.system(f"title Taken:{[takencount]}   Available:{[availablecount]}  Errors:{[errorcount]}")
def check():
 try:
  while True:
   openusers = open(username_file,"r").read().splitlines()
   for username in openusers:
    global availablecount, takencount, errorcount
    re = requests.post(f'https://instagram.com/{username}')
    if re.text.find(',"target_id":"') >= 0:
     takencount +=1
     print(f"/{Colors.red}X{Colors.reset}/ Taken: [{username}]")
    elif re.text == '':
     errorcount +=1
    else:
     availablecount +=1
     print(f"/{Colors.green}+{Colors.reset}/ Available: [{username}]")
 except:
  errorcount +=1
  pass
Thread(target=(title)).start()
Thread(target=(check)).start()
