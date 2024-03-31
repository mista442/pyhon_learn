'''
import telnetlib
telnet = telnetlib.Telnet('192.168.100.1')
In [2]: telnet.read_until(b'Username')
Out[2]: b'\r\n\r\nUser Access Verification\r\n\r\nUsername‚
In [3]: telnet.write(b'cisco\n')
In [4]: telnet.read_until(b'Password')
Out[4]: b': cisco\r\nPassword'
In [5]: telnet.write(b'cisco\n')
In [6]: telnet.read_until(b'>')
Out[6]: b': \r\nR1>'
In [7]: telnet.write(b'sh ip int br\n')
In [7]: telnet.read_until(b'>')
'''


'''
Import paramiko
In [2]: client = paramiko.SSHClient()
In [3]: client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
In [4]: client.connect(hostname="192.168.100.1", username="cisco", password="cisco", look_for_keys=False, allow_agent=False)
In [5]: ssh = client.invoke_shell()
In [7]: ssh.send("enable\n")
Out[7]: 7
In [8]: ssh.send("cisco\n")
Out[8]: 6
In [9]: ssh.send("sh ip int br\n")
ssh.recv(3000)
'''

'''
import netmiko
from netmiko import ConnectHandler
cisco_router = {
'device_type': 'cisco_ios',
'host': '192.168.100.1',
'username': ‘cisco',
'password': ‘cisco',
'secret': ‘cisco',
'port': 22,
}
ssh = ConnectHandler(**cisco_router)
ssh.enable()
result = ssh.send_command('show ip int br')
print(result)
'''