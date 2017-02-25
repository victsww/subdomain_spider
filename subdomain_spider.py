'''
@author: xiaoye
'''
import requests
import re
from bs4 import BeautifulSoup
from optparse import OptionParser

if __name__ == '__main__':
	parse = OptionParser()
	parse.add_option('-o', '--out', dest='outfile', type='string', help='output filename')
	parse.add_option('-d', '--domain', dest='domain', type='string', help='main domain')
	(option, args) = parse.parse_args()
	url = 'http://i.links.cn/subdomain/' + option.domain + '.html'
	print 'subdomain search...\nresult:\n'
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	r = requests.get(url, headers=headers)
	if r.status_code == 200:
		cont = r.content
	soup = BeautifulSoup(cont, 'lxml', from_encoding='gb2312')
	bqs = soup.find_all('a', rel='nofollow')
	#print bqs
	for bq in bqs:
		print bq.get_text().replace('http://', ' \n')
		if option.outfile != '':
			with open(option.outfile,'a') as f:
				f.write(bq.get_text().replace('http://', ' \n'))
