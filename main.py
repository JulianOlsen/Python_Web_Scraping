
"""
import scipy
import pandas
import numpy
"""
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

URL = "https://svk.jorsal.dk"
#page = requests.get(URL)
page = urlopen(URL)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

#print(html) #Prints the hole HTML of website

"""
title_index = html.find("<table cellpadding=5 border=1 bgcolor=#fff>")
start_index = title_index + len("<table cellpadding=5 border=1 bgcolor=#fff>")
end_index = html.find("</table>")
title = html[start_index:end_index]

print(title_index)
print(start_index)
print(end_index)
print(title)
"""

title_indexday = html.find("<table cellpadding=5 border=1 bgcolor=#fff><tr><td>Opdateret:</td><td align=right>")
start_indexday = title_indexday + len("<table cellpadding=5 border=1 bgcolor=#fff><tr><td>Opdateret:</td><td align=right>")
end_indexday = html.find("</td></tr><tr><td>Luft:</td>")
titleday = html[start_indexday:end_indexday]

"""
Date and Ti8me Index Test
print(title_indexday)
print(start_indexday)
print(end_indexday)
"""
print(titleday)


title_indexair = html.find("</td></tr><tr><td>Luft:</td><td align=right>")
start_indexair = title_indexair + len("</td></tr><tr><td>Luft:</td><td align=right>")
end_indexair = html.find("&deg;C</td></tr><tr><td>Vand:</td><td align=right>")
titleair = html[start_indexair:end_indexair]

"""
Air Index location
print(title_indexair)
print(start_indexair)
print(end_indexair)
"""
print(titleair)


title_indexwater = html.find("</td></tr><tr><td>Vand:</td><td align=right>")
start_indexwater = title_indexwater + len("</td></tr><tr><td>Vand:</td><td align=right>")
end_indexwater = html.find("&deg;C</td></tr></table>")
titlewater = html[start_indexwater:end_indexwater]

"""
water Index lacation test
print(title_indexwater)
print(start_indexwater)
print(end_indexwater)
"""

print(titlewater)


my_file = open("myfile.txt", "w")
print(my_file.write(titleday + "\n Air Temprature: " + titleair + "\n Water Temprature: " + titlewater + "\n"))

my_file.close()