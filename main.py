from colorama import Fore, init
import time
import requests
from datetime import datetime
from zoneinfo import ZoneInfo
import os

init(autoreset=True)

logo = f'''{Fore.LIGHTMAGENTA_EX} _____ _____ _____ _  __
/ ____|  _  / ____| |/ /
\___ \| |_) \___ \| ' / 
 ____) |  _ < ____) | . \\
|_____/|_| \\_\\_____/|_|\\_\\

{Fore.LIGHTRED_EX}Made by farfromsociety
{Fore.LIGHTYELLOW_EX}Github.com/farfromsociety
'''

def lookup(id_address, bot_token):
    url = f"https://discord.com/api/v10/users/{id_address}"
    
    headers = {
        "Authorization": f"Bot {bot_token}",
        "User-Agent": "DiscordBot (https://github.com/farfromsociety, 1.0.0)"
    }
    
    try:
        timestamp_ms = ((int(id_address) >> 22) + 1420070400000) / 1000
        creation_date = datetime.fromtimestamp(timestamp_ms, ZoneInfo("Europe/London")).strftime('%Y-%m-%d %H:%M:%S %Z')
    except ValueError:
        return None

    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            
            avatar_hash = data.get('avatar')
            avatar_url = f"https://cdn.discordapp.com/avatars/{id_address}/{avatar_hash}.png" if avatar_hash else "No Custom Avatar"
            
            banner_hash = data.get('banner')
            banner_url = f"https://cdn.discordapp.com/banners/{id_address}/{banner_hash}.png" if banner_hash else "Default"

            return {
                "Discord ID": id_address,
                "Username": data.get('username', "Not available"),
                "Display Name": data.get('global_name', "None"),
                "Avatar URL": avatar_url,
                "Banner URL": banner_url,
                "Accent Color": data.get('accent_color', "None"),
                "Public Flags": data.get('public_flags', "0"),
                "Bot Account": "Yes" if data.get('bot') else "No",
                "Creation Date": creation_date
            }
        else:
            return None
            
    except Exception:
        return None

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print(logo)
    
    bot_token = input(f"{Fore.LIGHTYELLOW_EX}Bot Token:{Fore.LIGHTWHITE_EX} ").strip()
    
    if not bot_token:
        exit()

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(logo)
        print(f"{Fore.LIGHTBLACK_EX}" + "─" * 45)
        
        ID = input(f"{Fore.LIGHTGREEN_EX}ID:{Fore.LIGHTWHITE_EX} ").strip()
        
        if not ID or not ID.isdigit():
            continue
            
        result = lookup(ID, bot_token)
        
        if not result:
            continue
        
        print(f"\n{Fore.LIGHTBLACK_EX}" + "─" * 45)
        for key, value in result.items():
            print(f"{Fore.LIGHTRED_EX} {key:<14}{Fore.LIGHTCYAN_EX}: {Fore.WHITE}{value}")    
        print(f"{Fore.LIGHTBLACK_EX}" + "─" * 45)
        
        input()