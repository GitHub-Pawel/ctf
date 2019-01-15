from scapy.layers.inet import IP, ICMP,  Ether
from scapy.sendrecv import sendp
import sys

def main():
    flag = "flag_{I7_W45_R34lly_Impr3551v3}"

    sendp(Ether(src='5e:c1:5c:00:13:57', dst='af:1a:91:5c:10:5e', type=0x88e5)/flag, loop=1000000, inter=1)

if __name__ == "__main__":
    main()
