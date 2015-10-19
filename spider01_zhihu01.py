import requests
import re


for i in xrange(1, 7):

	url = 'http://www.zhihu.com/topic/19577498?page=%s' % str(i)
	r = requests.get(url)

	select = re.compile(r'<a class="question_link" target="_blank" href="(.*?)">(.*?)</a>')

	html = r.text

	lst = select.findall(html)

	for i in lst:
		print 'address:  ', 'http://www.zhihu.com/' + i[0]
		print 'question: ', i[1]
