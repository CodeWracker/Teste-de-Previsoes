from datetime import *
hoje = date.today()
print(hoje)
data = date(2001,1,23)
print(data - timedelta(days=(365*2)))
for i in range(0,10):
    data = data + timedelta(days=1)
    print(data)