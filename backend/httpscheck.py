import requests
import re

def rmrf_protocol(urlts):
	urlts = re.sub("^(http|https)://", "", urlts)
	return urlts

def scan(urlts):
	urlts = rmrf_protocol(urlts)
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	urlts="http://"+urlts
	r = requests.get(urlts,headers=headers,timeout=5, allow_redirects=True) # first we try http
	print(r.url) # check the actual URL for the site

	if "https" in r.url:
		try:
			if "301" in str(r.history[0]):
				result="YES;HR"
				return result
			elif "302" in str(r.history[0]):
				result="YES;SR"
				return result
			else:
				result="YES;NR"
				return result
		except IndexError:
			print(IndexError)
			result = "YES;NR"
			return result
	else:
		result = "NO;NO"
		return result

# if __name__ == '__main__':
# 	res=scan('http://stackoverflow.com')
# 	res=res.split(';')
# 	print(res[0])
