import argparse
import pandas
import numpy
from scapy.all import rdpcap
from sklearn.neighbors import KNeighborsClassifier as KNN


# set up command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('data', help='pcap data')
args = parser.parse_args()

packets = rdpcap(args.data)
length = 0
for data in packets:
    if 'TCP' in data:
        length += len(data['TCP'].payload)


# set up training data and label
df = pandas.read_csv('result.csv')
trainmat = numpy.array(df['length']).reshape(42, 1)
label = numpy.array(df['type'])

# instantiate classifier and train data
model = KNN(n_neighbors=5)
model.fit(trainmat, label)

# use the model to predict
d = {'autolab': 1, 'bing': 2, 'canvas': 3, 'craigslist': 4, 'neverssl': 5, 'tor': 6, 'wikipedia': 7}
x_test = length
y_test = model.predict_proba([[x_test]])
for key, data in zip(d.keys(), y_test[0]):
    d[key] = data
for key in d.keys():
    print(str(key)+': ', d[key])

