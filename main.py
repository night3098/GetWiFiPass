import subprocess
try:
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp866').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All user profiles" in i]
    pass_wifi = ''
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode(
            'cp866').split('\n')
        for x in results:
            if "key content" in x:
                pass_wifi += f"{i} -- {x.split(':')[1][1:-1]}\n"
    print(pass_wifi)
except Exception as e:
    print(f'Sorry, an error has occurred. error name: {e}')
