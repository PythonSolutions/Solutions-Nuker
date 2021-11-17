

import requests
import json
import Solutions

from colorama import Fore
from util.plugins.common import setTitle, print_slow, getheaders, proxy

def MassDM(token, Message):
    headers = {'Authorization': token}
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    for channel in channelIds:
        try:
            setTitle(f"Messaging "+channel['id'])
            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
                proxies={"ftp": f'{proxy()}'},
                headers=headers,
                data={"content": f"{Message}"})
            print(f"{Fore.RED}Messaged ID: {Fore.WHITE}"+channel['id']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
    print_slow(f"{Fore.RED}Messaged available DM's.{Fore.RESET} ")
    print("Enter anything to continue. . . ", end="")
    input()
    Solutions.main()