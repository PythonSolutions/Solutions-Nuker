
import undetected_chromedriver as uc
import os
import Solutions
from time import sleep
from selenium import webdriver
from colorama import Fore
import Solutions



def TokenLogin(token):
    print(f"{Fore.GREEN}Checking Chromedriver. . .")
    sleep(0.5)
    if os.path.exists(os.getcwd()+"\\chromedriver.exe"):
        print("Chromedriver already exists, continuing. . .")
        sleep(0.5)
    else:
        try:
            print(f"{Fore.RED}Chromedriver not found! Installing it for you")
            uc.install()
        except Exception as e:
            print(f"{Fore.RED}Failed to download driver. . .\nError: {e}")
            print(f"")
            sleep(5)
            Solutions.main()
    try:
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opts)
        script = """
                function login(token) {
                setInterval(() => {
                document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
                }, 50);
                setTimeout(() => {
                location.reload();
                }, 1000);
                }
               """
        driver.get("https://discordapp.com/login")
        driver.execute_script(script+f'\nlogin("{token}")')
        Solutions.main()
    except Exception as e:
        print(f"{Fore.RED}Sorry Solutions had trouble logging ")
        print(f"Ignoring error: {e}")
        sleep(5)
        Solutions.main()
