from scapy.all import *
from scapy.layers.inet import TCP, IP

ans,unans=sr(IP(dst="10.1.5.100")/TCP(dport=80,flags="S") )
ans.summary(lambda s,r : r.sprintf("%IP.src% is alive") )

