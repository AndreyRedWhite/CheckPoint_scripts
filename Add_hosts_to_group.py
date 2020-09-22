hosts = '''
10.102.56.198
10.17.54.198
10.97.198.70
10.97.201.134
10.97.224.198
10.97.236.134
10.97.238.134
10.97.248.6
10.97.41.134
10.97.69.198
10.97.80.134
10.97.99.198
'''

parse_h = hosts.split()

# enter group name here
group_name = input("Enter the name of the group: ")

# vars for Auth
username = input("enter username for MGMT: ")
passwd = input("enter your pass for MGMT: ")
session_id = '-s id.txt'

# makes login to mgmt server, save session id in id.txt
print('mgmt_cli login -u {} -p {} > id.txt'.format(username, passwd))

i = 0
y = 1

output = 'mgmt_cli add group name "{}" '.format(group_name)

while i < len(parse_h):
    output = output + 'members.{} "h_{}" '.format(str(y), parse_h[i])
    i += 1
    y += 1
print(output + session_id)
