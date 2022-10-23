
import subprocess
import re
import platform


def read_data_from_cmd():
    p = subprocess.Popen("netsh wlan show networks mode=BSSID", stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    out = p.stdout.read().decode('unicode_escape').strip()
   
    if platform.system() == 'Linux':
        m = re.findall('(wlan[0-9]+).*?Signal level=(-[0-9]+) dBm', out, re.DOTALL)
    elif platform.system() == 'Windows':
        m = re.findall('SSID.*?:.*?([A-z0-9 ]*).*?Signal.*?:.*?([0-9]*)%', out, re.DOTALL)
       
    else:
        raise Exception('reached else of if statement')
    p.communicate()
    
    return m
print(read_data_from_cmd())