# names of hosts
names = '''
Mn-hdap05
Mn-hdap06
Mn-hdap07
Mn-hdap08
Mn-hdap09
Mn-k8sdev01
Mn-k8sdev05
Mn-k8sdev07
Mn-k8sdev08
Mn-k8sdev13
Mn-k8sdev14
Mn-k8sdev15
Mn-k8sdev16
Mn-k8sdev17
Mn-k8sdev18
Mn-k8sdev19
Mn-k8sdev20
Mn-rtx02
Mn-rtx03
Mn-rtx04
Mn-rtx05
Mn-k8sdev21
Mn-k8sdev22
Mn-k8sdev23
'''
hosts = '''
192.168.234.5
192.168.234.6
192.168.234.7
192.168.234.8
192.168.234.9
192.168.234.11
192.168.234.15
192.168.234.17
192.168.234.18
192.168.234.23
192.168.234.24
192.168.234.25
192.168.234.26
192.168.234.27
192.168.234.28
192.168.234.29
192.168.234.30
192.168.234.31
192.168.234.32
192.168.234.33
192.168.234.34
192.168.234.35
192.168.234.36
192.168.234.37
'''

# enter the group name here
group_name = input("Enter the name of the group: ")

output = 'mgmt_cli add group name "{}" '.format(group_name)

# vars for Auth
username = input("enter username for MGMT: ")
passwd = input("enter your pass for MGMT: ")

# makes login to mgmt server, save session id in id.txt
print('mgmt_cli login -u {} -p {} > id.txt'.format(username, passwd))

hostname = names.split()
host_ip = hosts.split()
api = 'mgmt_cli add host name '
i = 0
j = 0
y = 1
while i < len(hostname) and j < len(host_ip):
    # print(api + '"{}" ip-address {} '.format(hostname[i], host_ip[j]) + '-s id.txt --format json')
    output = output + 'members.{} "{}" '.format(str(y), hostname[i])
    i += 1
    j += 1
    y += 1

print(output + '-s id.txt --format json')
