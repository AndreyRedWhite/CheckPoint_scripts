# input all your hosts here. reqiured hosts in <ip address> format, for example '10.254.1.20'
urls = '''
ya.ru
*.mail.ru
'''
url_parse = urls.split()

# vars for Auth
username = input("enter username for MGMT: ")
passwd = input("enter your pass for MGMT: ")
session_id = '-s id.txt'
api = 'mgmt_cli add host name '

# makes login to mgmt server, save session id in id.txt
print('mgmt_cli login -u {} -p {} > id.txt'.format(username, passwd))

# creates list of commands to add all hosts from your list
for new_host in host_parse:
    print(api + '"h_{}"'.format(new_host) + ' ip-address {} '.format(new_host) + session_id)