# -*- coding: utf-8 -*-
class Ontology:
    """Ontology search on data.bioontology.org"""
    
    def __init__(self):
        self.BASE_URL = 'http://data.bioontology.org'
        self.API_KEY = '249a37ae-d343-431c-86c6-82a429f9b954' #urushibata.emerson@gmail.com
    
    def search(self, Q, EXACT = True, SUGGEST = True, ONTOLOGIES = 'EFO'): # OBI ontology
        import re
        
        r = self._get_json(self.BASE_URL, self.API_KEY, Q, EXACT, ONTOLOGIES, SUGGEST)
        if ('status' in r.keys() and r['status'] == 404):
            pass

        if ('pageCount' in r.keys() and r['pageCount'] >= 1):
            if('collection' in r.keys() and len(r['collection']) != 0):
                print('Total terms: '+str(len(r['collection'])))
                for idx,i in enumerate(r['collection']):
                    try:
                        assay_term_id = ':'.join(re.findall(r'\w+', i['@id'])[-1].split('_'))
                        i['term_id'] = assay_term_id
                        i['synonym'].append(i['prefLabel'])
                        print ("%s (%s)")%(assay_term_id, i['prefLabel'])
                        # print(i['synonym'])
                        # print(i['definition'])
                    except KeyError: pass
                return r['collection']
        # if EXACT == True:
            # self.search(Q, False, SUGGEST, ONTOLOGIES)
        # else:
        return []

    def _get_json(self, base_url, apikey, q, exact_match = True, ontologies = '', suggest = False):
        from string import Template
        import requests

        url_temp = Template('${_base_url}/search/?apikey=${_apikey}&q=${_q}&ontologies=${_ontologies}&pagesize=5000&include_links=false&exact_match=${_exact_match}&suggest=${_suggest}')
        url = url_temp.substitute(_base_url=base_url, _apikey=apikey, _q=q, _ontologies=ontologies, _exact_match=str(exact_match).lower(), _suggest=str(suggest).lower())
        return requests.get(url).json()