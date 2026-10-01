## Trying things with socket module
## A very basic scanner to grab banners, uses thread and screenLock for performance
## Specify a host and a port to scan

import socket
import optparse 
from socket import AF_INET, SOCK_STREAM
from threading import *

screenLock = Semaphore(value=1)

def conScan(tgtHost, tgtPort):
	try:
		# Creates the socket AF_INET for ipv4 and SOCK_STREAM for TCP. 
		connSkt = socket.socket(AF_INET, SOCK_STREAM)
		connSkt.settimeout(3)
		connSkt.connect((tgtHost, tgtPort))
		
		connSkt.send(b'GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n')
		banner = connSkt.recv(1024).decode()
		screenLock.acquire()
		
		print("%d/tcp open" % tgtPort)
		print("Response : " + str(banner))
	
	except socket.error as err:
		print ("socket creation failed with error %s" %(err))
		
	except:
		screenLock.acquire()
		print("%d/tcp closed" % tgtPort)

	finally:
		screenLock.release()
		connSkt.close()

def portScan(tgtHost, tgtPorts):
	# gethostbyname = fqdn -> IP
	try:
		tgtIp = socket.gethostbyname(tgtHost)
	except:
		print("Cannot resolve '%s' Unknown Host"%tgtHost)
		return
	try:
		tgtName = socket.gethostbyaddr(tgtIp)
		print("Scan Results for: " + tgtName[0])
	except:
		print("Scan results for :" + tgtIp)
	socket.setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target =conScan, args=(tgtHost, int(tgtPort)))
		t.start()
		print("Scanning port" + tgtPort)
		conScan(tgtHost, int(tgtPort))

def main():
	parser = optparse.OptionParser('usage %prog -H ' + '<target host> -p <taget port>')

	parser.add_option("-H", dest = "tgtHost", type="string", help="specify target host")
	parser.add_option("-p", dest="tgtPort", type="string", help="specify target port")
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(', ')

	if (tgtHost is None) or (tgtPorts[0] is None):
		print(parser.usage)
		exit(0)
	portScan(tgtHost, tgtPorts)

if __name__ == "__main__":
	main()
