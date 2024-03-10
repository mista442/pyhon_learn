import re

with open('sh_cdp_neighbors_sw2.txt') as f:
 sh_cdp = f.read()

regex = r'Device ID: (\S+).+?Platform: \w+ (\S+),.+?Cisco IOS Software.+?Version (\S+),'
match = re.finditer(regex, sh_cdp, re.DOTALL)
for m in match:
  print(m.groups())