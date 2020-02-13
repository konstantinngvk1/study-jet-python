from pysnmp.hlapi import *

snmp_object_1 = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_object_2 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

ip = '10.31.70.107'
port = '161'

result1 = getCmd(SnmpEngine(),
                 CommunityData('public', mpModel=0),
                 UdpTransportTarget((ip, port)),
                 ContextData(),
                 ObjectType(snmp_object_1))

result2 = nextCmd(SnmpEngine(),
                  CommunityData('public', mpModel=0),
                  UdpTransportTarget((ip, port)),
                  ContextData(),
                  ObjectType(snmp_object_2),
                  lexicographicMode=False)

print("\nЗапрос данных с '%s'..." % ip)
for y in result1:
    for str in list(y)[3]:
        print(str)

print("\n\nЗапрос MIB")
for y in result2:
    for str in list(y)[3]:
        print(str)
