import datetime
import pytz


# Return Date
d = datetime.date(2016,7,24)
print(d)


# Return Today Date
tday = datetime.date.today()
print("Today Date : ",tday)
print("Year : ",tday.year)
print("WeekDay : ",tday.weekday())         # Monday = 0 Sunday = 6
print("WeekDay : ",tday.isoweekday())      # Monday = 1 Sunday = 7


# Return Date After Day
tdelta = datetime.timedelta(days=7)
print(tday+tdelta)           # Date After 7 Days
print(tday-tdelta)           # Date Before 7 Days


# Return Days Between Two Dates
bday = datetime.date(2024,7,21)
till_bday = bday - tday
print(till_bday.days)
print(till_bday.total_seconds())


# Return Time
t = datetime.time(9,30,45,100000)
print(t)
print(t.hour)


# Return DateTime
dt = datetime.datetime(2016,7,26,12,30,45,100000)
tdelta1 = datetime.timedelta(days=7)
tdelta1 = datetime.timedelta(hours=12)
print(dt)
print(dt.date())
print(dt.time())
print(dt.year)
print(dt+tdelta)        # Return 7 day after dt
print(dt+tdelta1)       # Return 12 hours after dt


# Return Today DateTime
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utcnow)


# Return TimeZone
dt = datetime.datetime(2016,7,27,12,30,45,tzinfo=pytz.UTC)             # Convert Into StandardTimeZone
dt_now = datetime.datetime.now(tz=pytz.UTC)                            # Convert Into StandardTimeZone
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)        # Convert Into StandardTimeZone

dt_mtn = datetime.datetime.utcnow().astimezone(pytz.timezone('US/Mountain'))  # Convert Into US TimeZone

dt_mtn1 = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn1 = mtn_tz.localize(dt_mtn1)
dt_east = dt_mtn1.astimezone(pytz.timezone('US/Eastern'))

print(dt)
print(dt_now)
print(dt_utcnow)
print(dt_mtn)
print(dt_mtn.strftime('%B %d,%Y'))       # strftime() Convert DateTime To String
print(dt_east)

for tz in pytz.all_timezones:
    '''Print All Available TimeZone'''
    print(tz)



# Convert String To DateTime
dt_str = "July 26,2016"
dt = datetime.datetime.strptime(dt_str,"%B %d,%Y")      # strptime() Convert DateTime To DateTime
print(dt)