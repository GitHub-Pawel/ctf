from scapy.layers.inet import IP, ICMP,  Ether
from scapy.sendrecv import send
import sys

def main():
    flag = "FLAG_[Gr4t$_U_F0und_P4ck3t_W1th_Fl49]"
    broadcast_addr = raw_input('Get your broadcast address: ')
    send(IP(dst=broadcast_addr)/ICMP(type=34)/flag, loop=1000000, inter=1)

if __name__ == "__main__":
    main()
