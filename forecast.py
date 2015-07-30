import json
import urllib2
import time


response = urllib2.urlopen('https://api.forecast.io/forecast/7a8831d3e3ae2c88d8dc22c05ab2920a/55.8580,-4.2590?units=si')
html = response.read()
data = json.loads(html)

current_summary = data['currently']['summary']
minute_summary = data['minutely']['summary']
hourly_summary = data['hourly']['summary']
daily_summary = data['daily']['summary'] 

#print data
print time.strftime("%c")
print " "
print current_summary
print minute_summary
print hourly_summary
print daily_summary

