import re

def soapdataprocess(soapdata, **kw):
	print "soapfulfill.py 2"
	print kw
	a = soapdata
	b = re.sub("http://www.w3.org/2003/05/soap-envelope", "http://schemas.xmlsoap.org/soap/envelope/", a) 
	a = re.sub("http://www.w3.org/2001/XMLSchema", "http://yc/xsd", b)
	print a
	return a