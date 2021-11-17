

import requests
import Solutions
from colorama import Fore

from util.plugins.common import print_slow, getheaders, proxy

def SpamServers(token, Server_Name):
    count = 0
    for i in range(100):#change this to the amount of servers you want to create | Can create 200 servers but they need nitro for that
        try:
            #Create all the servers named whatever you want
            payload = {'name': f'{Server_Name}', 'region': 'europe', 'icon': None, 'channels': None}
            requests.post('https://discord.com/api/v7/guilds', proxies={"ftp": f'{proxy()}'}, headers=getheaders(token), json=payload)
            print(f"{Fore.BLUE}Created {Server_Name} #{i}.{Fore.RESET}")
        except Exception as e:
            print(f"The following exception has been encountered and is being ignored: {e}")
    print_slow(f"{Fore.LIGHTGREEN_EX}Successfully created {count} servers! ")
    print("Enter anything to continue. . . ", end="")
    input()
    Solutions.main()