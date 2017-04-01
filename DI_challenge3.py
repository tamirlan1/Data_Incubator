# import urllib
# from BeautifulSoup import *
import urllib2
import numpy as np
import re

url = 'http://www.cawater-info.net/aral/data/morpho_e.htm'

year = []
water_level = []
water_surface_area = []
volume = []
big_water_level = []
big_water_surface_area = []
big_volume = []
small_water_level = []
small_water_surface_area = []
small_volume = []
data = urllib2.urlopen(url)
for line in data:
	# MAIN SEA
	if line.startswith('<td width=156 class') or line.startswith('<td width=114 class'):
		b = re.search('(?<=\>)(.*?)(?=\<)', line).group(0)
		year.append(int(b))
	elif line.startswith('<td width=104 class'):
		b = re.search('(?<=\>)(.*?)(?=\<)', line).group(0)
		if len(b) < 8:
			water_level.append(float(b.replace(',','.')))
	elif line.startswith('<td width=118 class'):
		b = re.search('(?<=\>)(.*?)(?=\<)', line).group(0)
		if len(b) < 8:
			water_surface_area.append(float(b.replace(',','.')))
	elif line.startswith('<td width=100 class'):
		b = re.search('(?<=\>)(.*?)(?=\<)', line).group(0)
		if len(b) < 8:
			volume.append(float(b.replace(',','.')))

	# BIG SEA
	elif line.startswith('<td width=65 class'):
		b = re.search('(?<=\>)(.*?)(?=\<)', line).group(0)
		if len(b) < 8:
			big_water_level.append(float(b.replace(',','.')))
	elif line.startswith('<td width=82 class'):
		b = re.search('(?<=\>)(.*?)(?=\<)', line).group(0)
		if len(b) < 8:
			big_water_surface_area.append(float(b.replace(',','.')))
	elif line.startswith('<td width=68 class'):
		b = re.search('(?<=\>)(.*?)(?=\<)', line).group(0)
		if len(b) < 8:
			big_volume.append(float(b.replace(',','.')))

	# SMALL SEA
	elif line.startswith('<td width=67 class'):
		b = re.search('(?<=\>)(.*?)(?=\<)', line).group(0)
		if len(b) < 8:
			small_water_level.append(float(b.replace(',','.')))
	elif line.startswith('<td width=80 class'):
		b = re.search('(?<=\>)(.*?)(?=\<)', line).group(0)
		if len(b) < 8:
			small_water_surface_area.append(float(b.replace(',','.')))
	elif line.startswith('<td width=64 class'):
		b = re.search('(?<=\>)(.*?)(?=\<)', line).group(0)
		if len(b) < 8:
			small_volume.append(float(b.replace(',','.')))

total_water_level = [round(np.mean(a), 2) for a in zip(big_water_level, small_water_level)]
water_level.extend(total_water_level)
total_water_surface_area = [round(sum(a), 2) for a in zip(big_water_surface_area, small_water_surface_area)]
water_surface_area.extend(total_water_surface_area)
total_volume = [round(sum(a), 2) for a in zip(big_volume, small_volume)]
volume.extend(total_volume)

print len(year)
print year
print len(water_level)
print water_level
print len(water_surface_area)
print water_surface_area
print len(volume)
print volume

import matplotlib.pyplot as plt
plt.plot(year, water_level)
plt.ylabel('Water Level (meters)')
plt.xlabel('Years')
plt.title('Aral Sea Water Level Change (meters)')
plt.xlim([1910,2010])
plt.ylim([0, 60])
plt.show()

plt.plot(year, water_surface_area)
plt.ylabel('Water Surface Area (thousands km^2)')
plt.xlabel('Years')
plt.title('Aral Sea Water Surface Area Change (thousands km^2)')
plt.xlim([1910,2010])
plt.ylim([0, 70])
plt.show()

plt.plot(year, volume)
plt.ylabel('Volume (km^3)')
plt.xlabel('Years')
plt.title('Aral Sea VolumDIdasdasdadsasdasd2e Change (km^3)')
plt.xlim([1910,2010])
plt.ylim([0, 1100])
plt.show()