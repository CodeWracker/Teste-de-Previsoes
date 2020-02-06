import datetime
data = datetime.date(2001,1,23)
print(data - datetime.timedelta(days=(365*2)))
for i in range(0,10):
    data = data + datetime.timedelta(days=1)
    print(data)