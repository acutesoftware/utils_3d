import os 
import sys

from socket import *
network = '192.168.1.'

def get_network_device_info(ipadd):
    nme = ''
    if os.system("ping -n 1 " + ipadd + " > /dev/null 2>&1") == 0:
        try:
            nme = getfqdn(ipadd)
        except:
            nme = ''
    return nme

def main():
    with open ('netinfo.csv', 'w') as fop:
        for ip in range(1,254):
            full_ip = network + str(ip)
            nme = get_network_device_info(full_ip)
            if nme != '' and nme != full_ip:
                print(full_ip + ' = ' + nme)
                fop.write('"' + full_ip + '","' + nme + '"\n')



main()
