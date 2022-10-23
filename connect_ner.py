import subprocess
from list_wifi import read_data_from_cmd

def disconnect():
     p = subprocess.Popen("netsh wlan disconnect", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
     p.communicate()

def connect_wifi():
    m=read_data_from_cmd()
    m=dict(m)
    i=0
    while dict(list(m.items())[i:]):
        s=dict(list(m.items())[i:])
        max_wifi=max(s, key= lambda key: s[key])
    
        wifi_actuel=read_data_from_cmd()
        if(len(wifi_actuel)==0):
            wifi_actuel="no wifi"
        else:
            wifi_actuel=read_data_from_cmd()[-1][0]    
        msg=''
        
        
        try:
            p = subprocess.Popen("netsh wlan connect name="+max_wifi.strip() +" ssid="+max_wifi.strip(),stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if (wifi_actuel==max_wifi):
                msg="Vous etes connecté à "+str(max_wifi)
            else:
                p = subprocess.Popen("netsh wlan connect name="+ wifi_actuel +" ssid="+wifi_actuel,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("Vous etes connecté à "+str(wifi_actuel))
        except :
            msg="you don't have password for nearest wifi:"+str(max_wifi)
        
        i+=1

        print(wifi_actuel)
        if(wifi_actuel!="no wifi"):
            break
        return msg

connect_wifi()