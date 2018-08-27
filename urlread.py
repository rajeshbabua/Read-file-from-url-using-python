import urllib2
r = urllib2.urlopen("https://www.kaggle.com/blastchar/telco-customer-churn")
ra= r.read()
print (ra)
