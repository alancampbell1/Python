"""
Python Dates:

A date in Python is not a data type of its own but imported through a module entitled
datetime.
This allows us to work with dates as date objects.
"""

import datetime

#Returns the current date and time
x = datetime.datetime.now()
print(x)

#This is displayed as year, month, day, hour, minute, second and microsecond

#The following returns the year and name of weekday
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

#To create a date, we use the datetime() class constructor of the datetime module
#It requires 3 parameters to create a date: year, month, day

#It can also take parameters for time and timezone but this is optional

y = datetime.datetime(2020, 5, 17)
print(y)							#prints 2020-05-17 00:00:00

"""
The datetime object has a method for formatting date objects into readable strings.
The method is called strftime() and takes one parameter, format, to specify the
format of the returned string.
"""

z = datetime.datetime(2018, 6, 1)
print(z.strftime("%B"))				#Returns current month of the year

"""
The following is a breakdown of all legal format codes:
%a - weekday, short verson, e.g. Wed
%A - weekday, full version, e.g. Wednesday
%w - weekday as a number
%d - day of the month as a number
%b - month name, short version, e.g. Dec
%B - month name, full version
%m - month as a number
%y - year, short version, no century, e.g. 18
%Y - year, full version
%H - Hour 00-23
%I - Hour 00-12
%p - AM/PM
%M - Minute 00-59
%S - second 00-59
%f - microsecond
%z - UTC offset
%Z - Timezone, e.g. CST
%j - day number of year 001 -366
%U - week number of the year 00 - 53, sunday first
%W - week number of the year 00 - 53, monday first
%c - local version of date/time
%x - local version of date
%X - local version of time
%% - A % character

"""










