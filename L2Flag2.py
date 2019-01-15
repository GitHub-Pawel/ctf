from scapy.layers.inet import Ether
from scapy.sendrecv import sendp
from os import system
import subprocess
import time

def check_eth0_status():
    return str(subprocess.check_output("cat /sys/class/net/eth0/operstate", shell=True)).strip()

def main():
    flag = "flag_{I7_W45_R34lly_Impr3551v3}"
    while check_eth0_status() == "up":
        for i in range(5):
            sendp(Ether(src='5e:c1:5c:00:13:57', dst='af:1a:91:5c:10:5e', type=0x88e5)/flag)
        time.sleep(5)

if __name__ == "__main__":
    main()
