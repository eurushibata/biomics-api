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

class Roadmap():
    url = 'http://www.ncbi.nlm.nih.gov/geo/roadmap/epigenomics/?view=samples&&mode=csv'

    def run(self):
        print Utils().download(self.url)

        base_url = 'https://www.encodeproject.org'

    # url_antibody = 'https://www.encodeproject.org/search/?type=antibody_approval&limit=all&format=json'
    # url_sample = 'https://www.encodeproject.org/search/?type=biosample&limit=all&format=json'
    
    # raw = urlopen(url_experiment)
    # json_obj = json.load(raw)
    
    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017/')
    db = client['encode']

    # Force return in JSON format 
    HEADERS = {'accept': 'application/json'}

    # GET the object
    response = requests.get(urljoin(base_url, 'experiments/?limit=all'), headers=HEADERS)

    resp = response.json()

    for idx, n in enumerate(resp['@graph'][2681:]):
        time.sleep(1)
        respn = requests.get(urljoin(base_url, n['@id']), headers=HEADERS).json()
        q = db.experiment.insert(respn)
        sys.stdout.write(("\r%.3f%% - %s (%s)") % (((100.0/float(len(resp['@graph']))*(idx+1.0))), n['accession'], q))
        sys.stdout.flush()

