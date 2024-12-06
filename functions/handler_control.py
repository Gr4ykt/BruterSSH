from sys import exit, argv

#ctrl_c
def def_handler(sig, frame):
	print("\n[!]Saliendo de {}".format(argv[0]))
	exit(1)