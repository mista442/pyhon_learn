import re

mac_address_table = open('CAM_table.txt').read()
print(mac_address_table)

regex_1 = re.compile(r'\d+ +\S+ +\w+ +\S+')
regex_2 = re.compile(r'\d+ +(\S+) +\w+ +\S+')
regex_3 = re.compile(r'\d+ +(\S+) +\w+ +(\S+)')

print(regex_1.findall(mac_address_table))

print(regex_2.findall(mac_address_table))

print(regex_3.findall(mac_address_table))