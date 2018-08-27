  import urllib2
   import csv
   r= urllib2.urlopen("http://www.who.int/tb/country/data/download/en/")
   e= csv.reader(r)
   for row in e:
       print (row)
