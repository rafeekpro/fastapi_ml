from sklearn import linear_model
import json
import pickle

lr = linear_model.LinearRegression()

f = open('data.json')
data = json.load(f)

x_train = []
Y_train = []

for i in data['train_data']:
    x_train.append(i['features'])
    Y_train.append(i['result'])


# Closing file
f.close()

lr.fit(x_train, Y_train)    

pickle.dump(lr, open('model.pickle.sav', 'wb'))
