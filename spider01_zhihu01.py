# coding=utf-8
# __author__ = 'arvin'

import requests
import re


lst = []

for i in xrange(1, 50):

	url = 'http://www.zhihu.com/topic/19577498?page=%s' % str(i)
	r = requests.get(url)

	if r.status_code != 200:
		print 'THIS IS THE END!'
		break

	select = re.compile(r'<a class="question_link" target="_blank" href="(.*?)">(.*?)</a>')

	html = r.text


	results = select.findall(html)
	
	lst.extend(results)


for i in lst:
	address_lst = 'http://www.zhihu.com' + i[0]
	question_lst = i[1]

	print address.encode('utf-8')
	print question.encode('utf-8')
