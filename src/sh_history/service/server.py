#!/usr/bin/env python
import time,sys
from socket import socket,gethostname,AF_INET,SOCK_STREAM
def printstats(s,p,q,t):
	sys.stdout.write(f'\x1b[10G\x1b[1;34mHost:\x1b[0m\x1b[20G\x1b[1;29m{s}\x1b[0m')
	sys.stdout.write(f'\x1b[30G\x1b[1;34mPort:\x1b[0m\x1b[40G\x1b[1;29m{p}\x1b[0m\n')
	sys.stdout.write(f'\x1b[10G\x1b[1;34mMaxQ:\x1b[0m\x1b[20G\x1b[1;29m{q}\x1b[0m')
	sys.stdout.write(f'\x1b[30G\x1b[1;34mTime:\x1b[0m\x1b[40G\x1b[1;29m{t}\x1b[0m\n')
	sys.stdout.write(f'\x1b[10G\x1b[1;34mStatus:\x1b[0m\x1b[20G\x1b[1;5;32mRUNNING\x1b[0m\n')
	sys.stdout.flush()

def ts():
	return f'{time.ctime(time.time())}'

def sock(*a):
	#= 0.0.0.0 mor ipv4 en ipv6 compat
	# default poort (25) werkt niet op telenet(blocked)
	h=gethostname();host='';p=a[0];q=a[1];t=ts()
	s=socket(AF_INET,SOCK_STREAM);s.bind((host, p));s.listen(q)
	return s,h,p,q,t

def start(s,*a):
	csock, a = s.accept()
	print(f'{ts()}:\t{str(a)} connected.')
	data = csock.recv(1024)  # Read data sent by the client
	if data:
		print(f'Received data: {data.decode("utf-8")}')  # Print received data
	csock.close()

if __name__=='__main__':
	args=sys.argv
	print(args)
	if 1<  len(args) <3:p=int(args[1])
	elif len(args) == 3:p,q=args[1:]
	else:p,q=2525,10
	s,h,p,q,t=sock(int(p),int(q))
	printstats(h,p,q,t)
	while True:
		start(s);print(q-1)
