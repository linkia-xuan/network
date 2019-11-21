import os
import pandas
from scapy.all import rdpcap

# set up a dictionary to store seven kinds of web and training data
d = {'autolab': 1, 'bing': 2, 'canvas': 3, 'craigslist': 4, 'neverssl': 5, 'tor': 6, 'wikipedia': 7}
train = {'type': [], 'length': []}

file = os.listdir('PCAP')
#print(file)
for f in file:
    path = os.path.join('PCAP',f)
    packets = rdpcap(path)
    length = 0
    for data in packets:
        if 'TCP' in data:
            length += len(data['TCP'].payload)
    temp = f.split('.')
    train['type'].append(d[temp[0][:-1]])
    train['length'].append(length)

df = pandas.DataFrame(train)
df.to_csv('result.csv')




