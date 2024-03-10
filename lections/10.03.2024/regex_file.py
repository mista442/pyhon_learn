import re
regex = (r'Host \S+ in vlan (\d+) '
         r'is flapping between port '
         r'(\S+) and port (\S+)')

ports = set()
with open('log.txt') as f:
  for line in f:
    match = re.search(regex, line)
    if match:
        vlan = match.group(1)
        ports.add(match.group(2))
        ports.add(match.group(3))
print('Петля между портами {} в VLAN {}'.format(', '.join(ports), vlan))