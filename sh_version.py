#!/usr/bin/env python3

import paramiko
from netmiko import ConnectHandler
import re

#here is list of cisco routers ip addresses
ip_list = ['hostname or IP','hostname or IP']


#loop all ip addresses in ip_list
for ip in ip_list:
  cisco = {
    'device_type':'cisco_ios',
    'ip':ip,
    'username':'login username',     #ssh username
    'password':'login password',  #ssh password
  }
  
  net_connect = ConnectHandler(**cisco)

  # Set to the specific algorithms you require
  paramiko.Transport._preferred_kex = ('diffie-hellman-group14-sha1', 'diffie-hellman-group1-sha1')

# desired configuration set
  configuration = [
    'end',
    'show version',
    'show hardware',
    'show diag',
    'sh diag all eeprom',
    'sh diagnostic content',
    'sh diagnostic result slot all',
    'sh diagnostic schedule slot all',
    'sh diagnostic status',
    'sh diagnostic bootup level',
    'show module',
    'show idprom all',
    'show inv'
   ]

  
  #output = net_connect.send_command('show version')   # execute single command show version on router/switch and save output to output object
  output = net_connect.send_config_set(configuration)
 
   
  print(ip)    # print current ip address of router on screen
  print (output)  # print command result router on screen
  print("Requested task has been completed.") # inform user of completion
  net_connect.disconnect() #disconnet from the device
  
  
