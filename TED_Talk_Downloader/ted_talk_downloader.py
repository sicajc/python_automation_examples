import requests

from bs4 import BeautifulSoup

import re

import sys

# Exception handling,used to generalise the use of the code, anyone can code in the url from the terminal to execute this script
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error:Please enter the TED Talk URL")

#url = "https://www.ted.com/talks/sir_ken_robinson_do_schools_kill_creativity"


r = requests.get(url)

print("Download about to start")

soup = BeautifulSoup(r.content, features="lxml")

for val in soup.findAll('script id="__NEXT_DATA__" type="application/json"'):
    if(re.search("",str(val))) is not None:
        result = str(val)

result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")

mp4_url = result_mp4.split("")[0] #differnet quality exist

print("Downloading video from ....." + mp4_url)

file_name = mp4.url.split("/")[len(mp4.url.split("/")) - 1].split("?")[0]

print("Storing video in ....." + file_name)

r= requests.get(mp4_url)

with open(file_name,'wb') as f:
    f.write(r.content)

print("Download process finished")
