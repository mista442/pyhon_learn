# март

# 17 не встречаемся
# 24 удаленно
# 31 ?

#---------- продолженние изучения регулярок

import re

# log = 'Jun 3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'
#
# match = re.search(r'Host (\S+) in vlan (\d+) .* port (\S+) and port (\S+)',log)
#
# print(match) # <re.Match object; span=(46, 123), match='Host f03a.b216.7ad7 in vlan 10 is flapping betwee>
# print(match.group()) # Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15
#
# print(match.group(1)) # f03a.b216.7ad7
# print(match.group(2)) # 10
# print(match.group(3)) # Gi0/5
# print(match.group(4)) # Gi0/15
#
# tuple=match.group(1,2,3)
# print(tuple) # ('f03a.b216.7ad7', '10', 'Gi0/5')
#
# #-------------------------------
#
# match_2 = re.search(r'Host (\w{4}\.)+',log)
#
# print(match_2.group(1)) # b216. Отображает последнее попавшее совпадение

#------0----------------------------------------------------------------------------

# print()
#
# log = 'Jun 3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'
#
# match = re.search(r'Host (?P<mac>\S+) '
#  r'in vlan (?P<vlan>\d+) .* '
#  r'port (?P<int1>\S+) '
#  r'and port (?P<int2>\S+)', log)
# print(match.group('mac'))
# print(match.group('int2'))
#
# print(match.groups())
# print(match.groupdict()) # {'mac': 'f03a.b216.7ad7', 'vlan': '10', 'int1': 'Gi0/5', 'int2': 'Gi0/15'}, где mac - это имя шаблона, а f03a.b216.7ad7 это результат поиска попадающего под регулярку.

#---------------------------------------------------------

# line = '10 aab1.a1a1.a5d3 FastEthernet0/1'
# print(len(line)) # 33
# match = re.search(r'(\d+) +([0-9a-f.]+) +(\S+)', line)
#
# print(match.start()) # 0
# print(match.end()) # 33
#
# print(line[match.start():match.end()])
#
# print()
#
# #---------------------------------
#
# match = re.search(r'([0-9a-f.]+)', line)
#
# print(match.start())
# print(match.end())
#
# print(line[match.start():match.end()])

#-----------------------------------

# line = ' 10 aab1.a1a1.a5d3 FastEthernet0/1 '
# match = re.search(r'(\d+) +([0-9a-f.]+) +(\S+)', line)
# print(match.span()) # (1, 34)
#
# line = ' 10 aab1.a1a1.a5d3 FastEthernet0/1 '
# match = re.search(r'(\d+) +([0-9a-f.]+) +(\S+)', line)
# print(match.span(2)) # (4, 18)

#------------------------------------------

# log = '%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/16 and port Gi0/24'
# match = re.search(r'Host \S+ '
#  r'in vlan (\d+) '
#  r'is flapping between port '
#  r'(\S+) and port (\S+)', log)
#
# print(match.groups())

#-------------------------------------------

# regex = re.compile(r'\d+ +\S+ +\w+ +\S+')
# line = ' 100 a1b2.ac10.7000 DYNAMIC Gi0/1'
# match = regex.search(line)
# print(match.group())
#
# match = regex.search(line, 2)
# print(match.group())

#-------------------------------------------

# regex = re.compile(r'\d+ +\S+ +\w+ +\S+')
# line = ' 100 a1b2.ac10.7000 DYNAMIC Gi0/1'
# match = regex.search(line)
# print(match.group())
#
#
# match = regex.search(line, 2)
# print(match.group())
#
# match = regex.search(line[3:])
# print(match.group())
#
# match = regex.search(line, 2, 30)
# print(match.group())

#--------------------------------------------

# import re
# sh_cdp = '''
#  Device ID: SW2
#  Entry address(es):
#  IP address: 10.1.1.2
#  Platform: cisco WS-C2960-8TC-L, Capabilities: Switch IGMP
#  Interface: GigabitEthernet1/0/16, Port ID (outgoing port): GigabitEthernet0/1
#  Holdtime : 164 sec
#
#  Version :
#  Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9,RELEASE SOFTWARE (fc1)
#  Technical Support: http://www.cisco.com/techsupport
#  Copyright (c) 1986-2014 by Cisco Systems, Inc.
#  Compiled Mon 03-Mar-14 22:53 by prod_rel_team
# advertisement version: 2
#  VTP Management Domain: ''
#  Native VLAN: 1
#  Duplex: full
#  Management address(es):
#  IP address: 10.1.1.2
#  '''
# regex = r'Device ID: (\S+).+Platform: \w+ (\S+),.+Cisco IOS Software.+ Version (\S+),'
# match=re.search(regex, sh_cdp,re.DOTALL)
# print(match.groups())

#----------------------------------------------------

ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
print(re.split(r' +', ospf_route))
print(re.split(r'[,]+', ospf_route))
print(re.sub(r'(via|[,\[\]])', ' ', ospf_route))

#-----------------------------------------------------

mac_table = '''
 100 aabb.cc10.7000 DYNAMIC Gi0/1
 200 aabb.cc20.7000 DYNAMIC Gi0/2
 300 aabb.cc30.7000 DYNAMIC Gi0/3
 100 aabb.cc40.7000 DYNAMIC Gi0/4
 500 aabb.cc50.7000 DYNAMIC Gi0/5
 200 aabb.cc60.7000 DYNAMIC Gi0/6
 300 aabb.cc70.7000 DYNAMIC Gi0/7
 '''
print(re.sub(r' *(\d+) +'
 r'([a-f0-9]+)\.'
 r'([a-f0-9]+)\.'
 r'([a-f0-9]+) +\w+ +'
 r'(\S+)',
 r'\1 \2:\3:\4 \5',
 mac_table))