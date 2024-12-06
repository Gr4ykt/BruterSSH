#!/usr/bin/env python3

#     ++++++++++++++++++++++++++++++++
#     +                              +
#     +	          BruterSSH          +
#     +                              +
#     ++++++++++++++++++++++++++++++++
#			  Created by Gr4ykt
#	My Github ---> https://github.com/Gr4ykt

import signal, argparse
from pwn import *
from functions.handler_control import def_handler
from functions.ssh_brute import ssh_brute

signal.signal(signal.SIGINT, def_handler)
parser = argparse.ArgumentParser(description="SSH Brute")
parser.add_argument('-i', '--host', type=str, required=True)
parser.add_argument('-p', '--port', type=int, required=False, default=22)
parser.add_argument('-u', '--username', type=str, required=True)
parser.add_argument('-d', '--dir', type=str, required=True)
parser.add_argument('-t', '--threads', type=int, required=False, default=1)
args = parser.parse_args()

if __name__ == '__main__':
	ssh_brute(args.host, args.port, args.username, args.dir, args.threads)