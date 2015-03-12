# -*- coding: utf-8 -*-
from urllib2 import urlopen
from urlparse import urljoin
import json
import requests
import time
import sys
from pymongo import *


class Encode():
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
    # db.experiment.update({'accession': respn['accession']},
                    # respn,
                    # {'upsert': 'true'}
    # )
    # print(respn)
    # print(respn['files'][0]['file_format'])

    # print(respn['files'][1]['file_format'])
    # print(respn['files'][2]['file_format'])
    # print(respn['files'][3]['file_format'])






# print json.dumps(response_json_dict, indent=4, separators=(',', ': '))
