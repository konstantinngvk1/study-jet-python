import ipaddress, re
from glob import glob as glob


def Classifier(configs):
    ips_list = []

    for f in configs:
        with open(f) as file:
            for s in file:
                m = re.match("^ ip address ((?:[0-9]{1,3}\.?){4}) ((?:[0-9]{1,3}\.?){4})", s)
                i = re.match("^(interface)", s)
                h = re.match("^(hostname)", s)
                if m:
                    print("IP: ", m.group(1))
                    print('MASK: ', m.group(2))
                elif i:
                    print("INTERFACE: ", s)
                elif h:
                    print("\n\n-------------\n\nHOSTNAME: ", s) # Очень сильное колдунство



    return ips_list

h = Classifier(glob(".//config_files//*.txt"))
print(h)



