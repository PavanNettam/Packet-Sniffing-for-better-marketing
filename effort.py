from concurrent.futures import thread
from lib2to3.pytree import Node
import scapy.all as scapy
import threading 
import collections
import matplotlib.pyplot as plt

thread = None
should_we_stop = True
subdomain = ""
result = dict()

scr_ip_dict = collections.defaultdict(list)

def find_ips(packet):
    #print(packet.show())
    #print(packet[1].show())
    
    src_ip = packet.src
    dest_ip = packet.dst
    print(src_ip)
    print(dest_ip)
    if src_ip not in result:
        result[src_ip] = 0
    else:
        result[src_ip] += 1
    if src_ip[0:len(subdomain)] == subdomain:
        if src_ip not in src_ip_dict:
            scr_ip_dict[src_ip].append(dest_ip)
                
        else:
            if dest_ip not in scr_ip_dict[src_ip]:
                src_ip_dict[src_ip].append(dest_ip)
            
    #print(scr_ip_dict)
    print(result)
    k = list(result.keys())
    v = list(result.values())
    plt.bar(range(len(result)), v, tick_label=k)
    plt.show()  

def sniffing():
    scapy.sniff(prn=find_ips)

subdomain = input("Enter SubDomain: ")


if(thread is None) or (not thread.isalive()):
    should_we_stop = False
    thread = threading.Thread(target=sniffing)
    thread.start()

