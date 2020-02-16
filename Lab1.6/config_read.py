import ipaddress, re
from glob import glob as glob


def Classifier(configs):
    ips = []
    interfaces = []
    hosts = []
    for f in configs:
        with open(f) as file:
            for s in file:
                if re.match("^( ip address) ([0-9]{1,3}\.?){4} ([0-9]{1,3}\.?){4}$", s):
                    s = s.replace("ip address ", "")
                    t = re.split(" ", s)
                    net = ipaddress.IPv4Network((t[1], t[2].rstrip()), 0)
                    ip = {"ip": net}
                    ips.append(ip)
                elif re.match("^(interface)", s):
                    s = s.replace("interface ", "")
                    s = s.rstrip()
                    iface = {"int": s}
                    interfaces.append(iface)
                elif re.match("^(hostname)", s):
                    s = s.replace("hostname ", "")
                    s = s.rstrip()
                    host = {"host": s}
                    hosts.append(host)
    return ips, interfaces, hosts


i, inter, h = Classifier(glob(".//config_files//*.txt"))
print(i)
print(inter)
print(h)
