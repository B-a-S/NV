#/usr/bin/env python3
""" This app run a command, passed as parametres. on hosts
"""
import sys
from pssh.clients import ParallelSSHClient
hosts = ['host1' , 'host2']
client = ParallelSSHClient(hosts)
# client.password=""
# client.user=''
# client.pkey=""
print(sys.argv[1])
output = client.run_command(sys.argv[1])
for host_output in output:
    for line in host_output.stdout:
        print(line)
