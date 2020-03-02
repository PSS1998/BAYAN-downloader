import urllib.request

import bs4 as bs
import re
import sys

baseURL = input('Enter URL:')

source = urllib.request.urlopen(baseURL).read()
soup = bs.BeautifulSoup(source,'lxml')
result = soup.find_all(class_="single-video-title")
soup2 = bs.BeautifulSoup(str(result),'lxml')
filename = soup2.find("a").getText()

result = soup.find_all(class_="single-video")
soup2 = bs.BeautifulSoup(str(result),'lxml')
for script in soup2.find_all('script'):
	result = re.search(r'"https(.)*"', script.text)
	if result != None:
		result = result.group()
		baseURL = re.sub(r'playlist(.)*\?', f"144P/aaaaaa.ts?", result)

for i in range(1000):
	print(f"part {i+1}")
	URL = re.sub(r'aaaaaa', f"{i+1:03}", baseURL)
	try:
		response = urllib.request.urlopen(str(URL[1:-1]))
		if(response.getcode()==404):
			print("end")
			sys.exit()
		data = response.read()
		with open(filename + ".ts", "ab") as fp: fp.write(data)
	except:
		print("end")
		sys.exit()
