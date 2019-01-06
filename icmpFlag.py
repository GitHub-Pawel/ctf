from scapy.layers.inet import IP, ICMP,  Ether
from scapy.sendrecv import send
import sys

def main():
    flag = "FLAG_[Kn1ght5Wh0$4y-Nii]"
    send(Ether(src='01:23:45:67:89:0a', dst='ff:ff:ff:ff:ff:ff')/IP(dst="192.168.0.255")/ICMP(type=0)/flag, loop=100, inter=1)

if __name__ == "__main__":
    main()
