from flask.ext.script import Command
from urllib import urlencode
from urllib2 import urlopen, Request
from StringIO import StringIO

class Utils:

    def download(self, url):
        urldata = urlopen(url)
        file = StringIO(urldata.read())
        for line in file.readlines():
            print line


class Encode(Command):

    def run(self):
        url = 'https://spreadsheets.google.com/pub?key=0AvQL5qBL6AfEdFJqaU16U3JjT2hUX0JjeFFKVk56QlE&hl=en&output=csv'
        Utils().download(url)

class Roadmap(Command):

    def run(self):
        url = 'http://www.ncbi.nlm.nih.gov/geo/roadmap/epigenomics/?view=samples&&mode=csv'
        Utils().download(url)

class Tcga(Command):

    def run(self):
        url = 'https://tcga-data.nci.nih.gov/datareports/aliquotExport.htm'
        parameters = {'exportType': 'csv'}

        data = urlencode(parameters)
        request = Request(url, data)
        Utils().download(request)