import re

#findall - ищет все совпадения
#search - ищет только до первого совпадения

int_line = ' MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec,'
match = re.search(r'MTU', int_line)
print(match)

reg1="MTU"
reg2="BW \d+"
reg3="DLY"
match = re.search(reg1, int_line)
print(match.group())
match = re.search(reg2, int_line)
print(match.group())
match = re.search(reg3, int_line)
print(match.group())

'''
\d - одна цифра
+ - один или больше раз
\S - один символ (не пробел)
* - 0 или больше
? - 0 или 1
'''

log2 = 'Oct 3 12:49:15.941: %SW_MATM-4-MACFLAP_NOTIF: Host f04d.a206.7fd6 in vlan 1 is flapping between port Gi0/5 and port Gi0/16'
print(re.search(r'Host (\S+) in vlan (\d+) is flapping between port (\S+) and port (\S+)', log2).groups()) # groups - поиск значения по группе из нескольких регулярок. Которые указаны в (). То что идет вне () - игнорируется. В данном случае мы только показываем - в каком место строки применять регулярки.
print(re.search(r'Host \S+ in vlan (\d+) is flapping between port (\S+) and port (\S+)', log2).groups())

log = '*Jul 7 06:15:18.695: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/3, changed state to down'
print(re.search(r'\d\d:\d\d:\d\d', log).group())
print(re.search(r'\S{8}', log).group())

# group - поиск по одной группе регулярки
# groups - поиск по группе регулярных выражений

# ------------------------

text = """100  ИНФ  Информатика 213  МАТ  Математика 156  АНГ  Английский"""

# найти код всех предметов (3 варианта)
print(re.findall('\d\d\d',text))
print(re.findall('\d{3}',text))
print(re.findall('[0-9]+',text))

# найти аббревиатуру всех предметов

print(re.findall('\s\D{3}\s',text))
print(re.findall('[А-ЯЁ]{3}',text))

# найти названия предметов

print(re.findall('[А-ЯЁ][а-яё]+',text))
print(re.findall('[а-яА-ЯёЁ]{4,}',text))

                    #1           #2              #2           отдельные регулярки разделяются () и потом объединяются в один общий патерн
course_pattern = '([0-9]+)\s*([А-ЯЁ]{3})\s*([а-яА-ЯёЁ]{4,})'
print(re.findall(course_pattern, text))

#-------------------------------------------

log2 = 'Jun 3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'
print(re.search(r'\w\w\w\w\.\w\w\w\w\.\w\w\w\w', log2).group())
line = '100 aab1.a1a1.a5d3 FastEthernet0/1'
print(re.search(r'a+', line).group())
print(re.search(r'(a1)+', line).group())
#print(re.findall(r'a+', line)).group()

#-------------------------------------------

sh_ip_int_br = 'Ethernet0/1 192.168.200.1 YES NVRAM up up'
print(re.search(r'\d+\.\d+\.\d+\.\d+', sh_ip_int_br).group())

#------------------------------------------

email1 = 'user1@gmail.com'
email2 = 'user2.test@gmail.com'
print(re.search(r'\w+\.*\w+@\w+\.\w+', email1).group())
print(re.search(r'\w+\.*\w+@\w+\.\w+', email2).group())

#-------------------------------------------

mail_log = ['Jun 18 14:10:35 client-ip=154.10.180.10 from=user1@gmail.com, size=551', 'Jun 18 14:11:05 client-ip=150.10.180.10 from=user2.test@gmail.com, size=768']

for message in mail_log:
    match = re.search(r'\w+\.?\w+@\w+\.\w+', message)
    if match:
       print("Found email: ", match.group())

#------------------------------------------

mac_table = '''
...: sw1#sh mac address-table
...: Mac Address Table
...: -------------------------------------------
...:
...: Vlan Mac Address Type Ports
...: ---- ----------- -------- -----
...: 100 a1b2.ac10.7000 DYNAMIC Gi0/1
...: 200 a0d4.cb20.7000 DYNAMIC Gi0/2
...: 300 acb4.cd30.7000 DYNAMIC Gi0/3
...: 1100 a2bb.ec40.7000 DYNAMIC Gi0/4
...: 500 aa4b.c550.7000 DYNAMIC Gi0/5
...: 1200 a1bb.1c60.7000 DYNAMIC Gi0/6
...: 1300 aa0b.cc70.7000 DYNAMIC Gi0/7
...: '''

for line in mac_table.split('\n'):
  match = re.search(r'\d{1,4} +', line)
  if match:
    print('VLAN: ', match.group())

print(re.findall('\s\d{1,4}\s', mac_table))

#--------------------------------------------

cdp = '''
...: SW1#show cdp neighbors detail
...: -------------------------
...: Device ID: SW2
...: Entry address(es):
...: IP address: 10.1.1.2
...: Platform: cisco WS-C2960-8TC-L, Capabilities: Switch IGMP
...: Interface: GigabitEthernet1/0/16, Port ID (outgoing port): GigabitEthernet0/1
...: Holdtime : 164 sec
...: '''
print(re.search(r'Interface.+Port ID.+', cdp).group())

#---------------------------------------------

line = "100 aa12.35fe.a5d3 FastEthernet0/1"
print(re.search(r'^\d+', line).group())

#----------------------------------------------

commands = ['SW1#show cdp neighbors detail','SW1>sh ip int br','r1-london-core# sh ip route']

for line in commands:
 match = re.search(r'^.+[>#]', line)
 if match:
   print(match.group())

#----------------------------------------------

line = "100 aa12.35fe.a5d3 FastEthernet0/1"
print(re.search(r'[0-9]{1,4}', line).group())

print() #----------------------------------------------

line = "100 aa12.35fe.a5d3 FastEthernet0/1"
print(re.search(r'[a-f0-9]+\.[a-f0-9]+\.[a-f0-9]+', line).group())

print() #-------------------------------------------------

line = 'FastEthernet0/0 15.0.15.1 YES manual up up'
print(re.search(r'[^a-zA-Z]+', line).group())

print() #--------------------------------------------------

line = "100 aa12.35fe.a5d3 FastEthernet0/1"
print(re.search(r'[0-9]([a-f]|[0-9])[0-9]', line).group())

line1 = 'FastEthernet0/0 15.0.15.1 YES manual up up'
print(re.search(r'([0-9]+\.)+[0-9]+', line1).group())

print() #-----------------------------------------------

line = '<text line> some text>'
match = re.search(r'<.*>', line)
print(match.group())

print() #------------------------------------------------

line = '1500 aab1.a1a1.a5d3 FastEthernet0/1'
print(re.search(r'\d+\s+\S+', line).group())

print(re.search(r'\d+\s+\S+?', line).group())

print() #-------------------------------------------------

line = "FastEthernet0/1 10.0.12.1 YES manual up up"
match = re.search(r'(\S+)\s+([\w.]+)\s+.*', line)

print(match.group(0)) # вся стрка
print(match.group(1)) # результат первого регулярного выражения. Обращаемся к определенной регулярке
print(match.group(2)) # # результат первого регулярного выражения

print() #---------------------------------------------------

line1 = "FastEthernet0/1 10.0.12.1 YES manual up up"
match1 = re.search(r'(?P<intf>\S+)\s+(?P<address>[\d.]+)\s+', line1)
print(match1.group('intf'))
print(match1.group('address'))

print() #----------------------------------------

regex = r'(?P<mac>\S+) +(?P<ip>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<port>\S+)'
result = []
with open('dhcp_snooping.txt') as data:
  for line in data:
    match = re.search(regex, line)
    if match:
      result.append(match.groupdict())
print('К коммутатору подключено {} устройства'.format(len(result)))
for num, comp in enumerate(result, 1):
    print('Параметры устройства {}:'.format(num))
    for key in comp:
     print('{:10}: {:10}'.format(key, comp[key]))

print() #----------------------------------------------

log = 'Jun 3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'
match = re.search(r'((?:\w{4}\.){2}\w{4}).+vlan (\d+).+port (\S+).+port (\S+)', log)
print(match.groups())