from ipaddress import IPv4Address, IPv4Network
import random


class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        ip = random.randint(0x0B000000, 0xDF000000)
        mask = random.randint(8, 24)
        IPv4Network.__init__(self, (ip, mask), strict=False)




i=1
list_ip=[]


while i <= 5:
    net = IPv4RandomNetwork()
    list_ip.append(net)
    i=i+1


def key_value(self):
    return (self.netmask, self.network_address)


def convert(list_ip):
    c_list = []
    for i in list_ip:
        c_list.append(key_value(i))
    return c_list


def sortrandom(list_ip):
    sorted_list_ip = []
    for i in sorted(convert(list_ip)):
      sorted_list_ip.append(i)
    return sorted_list_ip

for a in sortrandom(list_ip):print(a)