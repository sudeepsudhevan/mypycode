import datetime

now=datetime.datetime.now()
print(now.strftime("%d/%m/%Y"))

print(datetime.date.today())

x=datetime.datetime(2023,month=4,day=17)
y=datetime.datetime(2023,month=4,day=1)

dif=x-y

print(dif)

end=datetime.datetime.now()

differnce=end-now

print(differnce)