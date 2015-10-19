# -*- coding: utf-8 -*-

__author__ = 'arvin'

#this program is get the answer of a question

import requests
import re


lst = []

url = 'http://www.zhihu.com/question/33946642'
r = requests.get(url)

html = r.text

vote_count_search = re.compile(r'<span class="count">(\d*?)</span>')

vote_count_num = vote_count_search.findall(html)

#get the  vote_num
for i in vote_count_num:
	print i
