from scapy.all import*

def LaunchAttack(src,dst,iface,count):
	#ip = IP(src=src, dst=dst)
	#icmp = ICMP(type=8, id=678)
	#data = Raw(load='1234')
	#pkt = ip/icmp/data
	#send(pkt, iface=iface, count=count)

	#tfn
	#pkt = IP(src=src, dst=dst)/ICMP(type=8, id=678)/Raw(load='1234')
	#send(pkt, iface=iface, count=count)

	#tfn2k
	#pkt = IP(src=src, dst=dst)/ICMP(type=0, id=0)/Raw(load='AAAAAAAAAA')	
	#send(pkt, iface=iface, count=count)

	#ntalkd
	#data = Raw(load=b'\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8')
	#pkt = IP(src=src, dst=dst)/UDP(dport=518)/data
	#send(pkt, iface=iface, count=count)

	#mountd overflow
	#data = Raw(load=b'^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F')
	#pkt = IP(src=src, dst=dst)/UDP(dport=635)/data
	#send(pkt, iface=iface, count=count)
	
	#Nmap XMAS
	#pkt = IP(src=src, dst=dst)/TCP(flags='FPU')
	#send(pkt, iface=iface, count=count)
	
	#SolarWinds IP scan
	#pkt = IP(src=src, dst=dst)/ICMP(code=0, type=8)/Raw(load='SolarWinds.Net')
	#send(pkt, iface=iface, count=count)
	
	#SYN FIN
	#pkt = IP(src=src, dst=dst)/TCP(flags='SF')
	#send(pkt, iface=iface, count=count)

	#Cybercop UDP bomb
	#pkt = IP(src=src, dst=dst)/UDP(dport=7)/Raw(load='cybercop')
	#send(pkt, iface=iface, count=count)

src = '1.2.3.4'
dst = '8.8.8.8'
#dst = '10.100.247.113'
iface = 'enp0s3'
count = 2
LaunchAttack(src,dst,iface,count)
