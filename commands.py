from flask.ext.script import Command
from urllib import urlencode
from urllib2 import urlopen, Request
from StringIO import StringIO
import json

class Utils:
    def download(self, url):
        l = list()
        urldata = urlopen(url)
        file = StringIO(urldata.read())
        x = file.readline()
        header = x.replace("\"", '').rsplit('\n')[0].rsplit('\r')[0].rsplit(',') # extract header from csv
        # blueprint = dict((k,'') for k in header) # creates blueprint for db
        for line in file.readlines():
            l.append(dict(zip(header,line.replace("\"", '').rsplit('\n')[0].rsplit('\r')[0].rsplit(','))))
        return json.JSONEncoder().encode(l)

class Encode(Command):
    url = 'https://spreadsheets.google.com/pub?key=0AvQL5qBL6AfEdFJqaU16U3JjT2hUX0JjeFFKVk56QlE&hl=en&output=csv'
        
    def run(self):
        print Utils().download(self.url)


class Roadmap(Command):
    url = 'http://www.ncbi.nlm.nih.gov/geo/roadmap/epigenomics/?view=samples&&mode=csv'

    def run(self):
        print Utils().download(self.url)

class Tcga(Command):
    url = 'https://tcga-data.nci.nih.gov/datareports/aliquotExport.htm'
    # url = 'http://www.ncbi.nlm.nih.gov/geo/roadmap/epigenomics/?view=samples&&mode=csv'

    def run(self):
        parameters = {'exportType': 'csv'}
        data = urlencode(parameters)
        request = Request(self.url, data)
        print Utils().download(request)

if __name__ == '__main__':
    Encode().run()