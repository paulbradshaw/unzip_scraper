import scraperwiki
#yep
#this is used to unzip the files: https://docs.python.org/2/library/zipfile.html
import zipfile
#this is used to temporarily store the file: https://docs.python.org/2/library/tempfile.html
import tempfile
#to open the url
import urllib
#to read the csv files within the zip
import csv

#Here we've got a few files to try. 


#this one is much smaller, so should run quicker
zipped = 'https://data.police.uk/data/archive/2013-05.zip'
#this is most recent
#but it's too big: Run killed by ScraperWiki, taking more than 1 hour, and wouldn't exit upon request
zipped = 'https://data.police.uk/data/archive/2017-01.zip'
#This is one year earlier
zipped = 'https://data.police.uk/data/archive/2016-01.zip'

#create an empty dictionary and idno variable used later
record ={}
idno = 0
#define a function to open the zip file and scrape the contents
#some of this code inspired by Tony Hirst's scraper at https://classic.scraperwiki.com/editor/raw/clinicaltrialsgov_test
def getFiles(lurl,idno):
    #create a temporary named file ending in '.zip' in new variable t
    t = tempfile.NamedTemporaryFile(suffix=".zip")
    #write the contents of the URL to t
    t.write(urllib.urlopen(lurl).read())
    #use seek to set starting point at beginning: https://www.tutorialspoint.com/python/file_seek.htm
    t.seek(0)
    #store the name(s) of the zip file in z?
    z = zipfile.ZipFile(t.name)
    print z
    #loop through the items
    for nz in z.namelist():
        print nz
        #e.g. 2011-04/2011-04-north-wales-street.csv
        #read into a new object?
        yearmonth = nz[0:7]
        print yearmonth
        if yearmonth != "2011-03":
            csvs=z.read(nz)
            #use csv reader to split that object on each line
            reader = csv.DictReader(csvs.splitlines())
            print reader
            for row in reader:
                #first column contains crime ID
                '''record['Crime ID'] = row[0]
                record['Month'] = row[1]
                record['Reported by'] = row[2]
                record['Falls within'] = row[3]
                record['lng'] = row[4]
                record['lat'] = row[5]
                record['Location'] = row[6]
                record['LSOA code'] = row[7]
                record['LSOA name'] = row[8]
                record['Crime type'] = row[9]
                record['Last outcome category'] = row[10]
                record['Context'] = row[11]'''
                idno = idno+1
                record['id'] = idno
                #scraperwiki.sqlite.save(['id'], record)
                scraperwiki.sqlite.save(['id'], row)
    #return z

#run the function
getFiles(zipped,idno)
