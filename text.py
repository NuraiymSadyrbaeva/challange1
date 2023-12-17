import ipaddress

# Netzwerk und Subnetzmaske definieren
netzwerk = ipaddress.ip_network('192.168.0.0/24')

# Alle IP-Adressen im Netzwerk ausgeben
for ip in netzwerk.hosts():
    print(ip)
#....


# Prüfen, ob eine IP-Adresse in einem bestimmten Bereich liegt
ip = ipaddress.ip_address('192.168.1.10')
netzwerk = ipaddress.ip_network('192.168.1.0/24')

if ip in netzwerk:
    print(f"Die IP-Adresse {ip} liegt im Netzwerk.")
else:
    print(f"Die IP-Adresse {ip} liegt nicht im Netzwerk.")
#....


# Details eines Netzwerks anzeigen
netzwerk = ipaddress.ip_network('192.168.0.0/24')

print(f"Netzwerkadresse: {netzwerk.network_address}")
print(f"Broadcast-Adresse: {netzwerk.broadcast_address}")
print(f"Anzahl der Hosts: {netzwerk.num_addresses}")
#...

# Generiere eine Liste von IP-Adressen in einem Bereich
start_ip = ipaddress.ip_address('192.168.0.1')
end_ip = ipaddress.ip_address('192.168.0.10')

for ip in range(int(start_ip), int(end_ip) + 1):
    print(ipaddress.ip_address(ip))
#hier habe ich test für ip adressen
#morgen werde ich besser lernen