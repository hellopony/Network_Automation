#!/usr/bin/env python3

import paramiko
from netmiko import ConnectHandler
from getpass import getpass

# Prompt for username and password
username = input("Username: ")
password = getpass()
device = input("Router/Switch name/IP? ")

# node aka router or switch connection information
node = {
'device_type': 'cisco_ios',
'host': device,
'username': username,
'password': password
}

# establish connection
ssh = ConnectHandler(**node)

# Set to the specific algorithms you require
paramiko.Transport._preferred_kex = ('diffie-hellman-group14-sha1', 'diffie-hellman-group1-sha1')

# desired configuration set
configuration = [
    'end',
    'show version',
    'show hardware',
    'show diag'
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

# push configuration set to the node
#ssh.send_config_set(configuration)

# show command history
output = ssh.send_config_set(configuration)
print (output)

# inform user of completion
print("Requested task has been completed.")

# disconnect from node
ssh.disconnect()
