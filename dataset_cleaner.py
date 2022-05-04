from io import StringIO


fh = open('used_car_price_data_short.txt')
data = []

for line in fh:
    data.append(line.split(","))

print(data)

for value in data:
    value[0] = int(value[0])
    value[1] = int(value[1])
    if value[2] == 'Good Deal\n':
        value[2] = 1
    elif value[2] == 'Great Deal\n':
        value[2] = 1
    elif value[2] == 'Good Deal \n':
        value[2] = 1
    elif value[2] == 'Great Deal \n':
        value[2] = 1
    elif value[2] == 'Good Deal':
        value[2] = 1
    else:
        value[2] = -1

    strlst = ','.join(str(e) for e in value)
    with open('clean_dataset.txt', 'a') as wf:
        wf.write(strlst + "\n")