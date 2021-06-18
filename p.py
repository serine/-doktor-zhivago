#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup

id = sys.argv[1]
base_url = 'https://boris-pasternak.su/proza/doktor-zhivago'
url = '{}/{}/'.format(base_url, str(id))
res = requests.get(url)
html_page = res.content

soup = BeautifulSoup(html_page, 'html.parser')

p_tags = soup.findAll('p')

header = False

for tag in p_tags:
    if  "КНИГА" in tag.text:
        print(str(tag).strip().replace("<p>", "#").replace("</p>", "") + " {-}")
        print()
    elif "ЧАСТЬ" in tag.text:
        print(str(tag).replace("<p>", "## ").replace("</p>", "").replace("<br/>", "") + " {-}")
        print()
    elif tag.text.isnumeric():
        header = True
        print(str(tag).strip().replace("<p>", "### ").replace("</p>", "") + " {-}")
        print()
    elif header:
        header = False
        print(str(tag).replace("<p>", "").replace("</p>", "").strip())
        print()

#if "ПЕРВАЯ КНИГА" in p_tags[0].text:
#    #info = p_tags[0:4]
#    print(str(p_tags[0]).strip().replace("<p>", "# ").replace("</p>", "") + " {-}")
#    print()
#    print(str(p_tags[1]).replace("<p>", "## ").replace("</p>", "").replace("<br/>", "") + " {-}")
#    print()
#    print(str(p_tags[2]).replace("<p>", "### ").replace("</p>", "") + " {-}")
#    print()
#    print(str(p_tags[3]).replace("<p>", "").replace("</p>", "").strip())
#elif "ЧАСТЬ" in p_tags[0].text or "ЧАСТЬ" in p_tags[1].text or "ЧАСТЬ" in p_tags[2].text:
#    #info = p_tags[0:3]
#    print(str(p_tags[0]).strip().replace("<p>", "## ").replace("</p>", "") + " {-}")
#    print()
#    print(str(p_tags[1]).replace("<p>", "### ").replace("</p>", "").replace("<br/>", "") + " {-}")
#    print()
#    print(str(p_tags[2]).replace("<p>", "").replace("</p>", "").strip())
#    #print()
#    #print(str(info[3]).replace("<p>", "").replace("</p>", "").strip())
#else:
#    #info = p_tags[0:3]
#    print(str(p_tags[0]).replace("<p>", "### ").replace("</p>", "") + " {-}")
#    print()
#    print(str(p_tags[1]).replace("<p>", "").replace("</p>", "").strip())
