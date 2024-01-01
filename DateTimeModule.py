import datetime as dt
#now()
now=dt.datetime.now()
print(now)

d=dt.datetime(2022,3,30,12,12,12)
print(d)

#strftime
now=dt.datetime.now()
print(now)
print("Month In short =",now.strftime("%b"))
print("Month In Full =",now.strftime("%B"))
print("Month In Number =",now.strftime("%m"))
print("Year In short =",now.strftime("%y"))
print("Year In Full =",now.strftime("%Y"))
print("Hours In 00-23 =",now.strftime("%H"))
print("Hours In 00-12 =",now.strftime("%I"))
print("AM/PM =",now.strftime("%p"))
print("Minutes =",now.strftime("%M"))
print("Seconds =",now.strftime("%S"))
