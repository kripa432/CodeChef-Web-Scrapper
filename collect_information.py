import urllib2
import urllib3
import certifi

import lxml
import csv
import ssl
from bs4 import BeautifulSoup
arr=[]
###reading input file
with open('codechef.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print row['CodeChef handle']
		arr=arr+[[row['CodeChef handle'],row['Year']]]

#arr=[['kripa432','3rd year'],['shubhmsng','3rd year'],['ajay532','3rd year'],['avmnusng','3rd year']]
#arr=['500']

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
#r = http.request('GET', 'http://example.com/')
#if r.status==200:
#	print "200"
#else:
#	print "error"
#html=r.data
##opening writing file
with open('Programmers of IERT.csv', 'w') as csvfile:
	fieldnames = ['handle', 'Year','Problems Solved','Problems Partially Solved','Solutions Submitted','Solutions Partially Accepted','Solutions Accepted','WA','CTE','RTE','TLE']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for i in arr:

		url="https://www.codechef.com/users/"+i[0];
		print url
		html=''
		try:
			#html=urllib2.urlopen(url)
			r=http.request('GET',url,retries=urllib3.Retry(1, redirect=False))
			if r.status==200:
				print "200"
			else:
				print "error"
			html=r.data

		except urllib2.HTTPError as e:
			print e.code
			print e.read()
			arr=arr+[i]
			continue
		#if html.geturl() <> url:
		#	print "incoorect username"
		#	continue;
		print r.status
		if r.status<>200:
			print "incorrect username"
			continue
		#soup = BeautifulSoup(html.read(),"lxml")
		soup = BeautifulSoup(html,"lxml")


		for tr in soup('table', {'id': 'problem_stats'})[0]('tr'):
			for td in tr('td'):
				print td.renderContents()

#extract single item
		ps=soup('table', {'id': 'problem_stats'})[0]('td')[9].renderContents()
		pps=soup('table', {'id': 'problem_stats'})[0]('td')[10].renderContents()
		ss=soup('table', {'id': 'problem_stats'})[0]('td')[11].renderContents()
		spa=soup('table', {'id': 'problem_stats'})[0]('td')[12].renderContents()
		sa=soup('table', {'id': 'problem_stats'})[0]('td')[13].renderContents()
		wa=soup('table', {'id': 'problem_stats'})[0]('td')[14].renderContents()
		cte=soup('table', {'id': 'problem_stats'})[0]('td')[15].renderContents()
		rte=soup('table', {'id': 'problem_stats'})[0]('td')[16].renderContents()
		tle=soup('table', {'id': 'problem_stats'})[0]('td')[17].renderContents()
##writing output file
	
		
		writer.writerow({'handle':i[0],'Year':i[1], 'Problems Solved':ps ,'Problems Partially Solved':pps,'Solutions Submitted':ss,'Solutions Partially Accepted':spa,'Solutions Accepted':sa,'WA':wa,'CTE':cte,'RTE':rte,'TLE':tle})
	