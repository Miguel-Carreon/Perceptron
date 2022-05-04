import pandas

data = pandas.read_csv("Used_Car_Price_Data.csv")

data = data.drop(['Name'], axis = 1)
data = data.drop(['Review'], axis = 1)
data = data.drop(['Review_count'], axis = 1)

data = data[data['Badge'].notnull()]
data.drop(data[data['Badge'] == 'CPO Warrantied'].index, inplace = True)
data.drop(data[data['Badge'] == 'Home Delivery'].index, inplace = True)
data.drop(data[data['Badge'] == 'Hot Car'].index, inplace = True)

data.replace(',', '', regex=True, inplace=True)

data.to_csv('used_car_price_data_short.csv', index = False)