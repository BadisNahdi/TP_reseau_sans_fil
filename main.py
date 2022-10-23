from list_wifi import *

m=read_data_from_cmd()

m=dict(m)
print(m)
max_wifi=max(m, key= lambda key: m[key])
print(max_wifi)

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
            wifi_actuel=read_data_from_cmd()[0][-1]    
        i+=1
        print(max_wifi)
        
       
        