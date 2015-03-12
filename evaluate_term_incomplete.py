for idx, n in enumerate(resp['@graph']):
        # time.sleep(1)
        if ('biosample_term_name' in n.keys()):
                term = n['biosample_term_name']
                print ("%s (%s) (%s)")%(term, n['assay_term_name'],n['accession'])
                a = Ontology.Ontology().search(term, False, False)
                print "====="


for idx, n in enumerate(resp['@graph']):
        # time.sleep(1)
        if ('biosample_term_name' in n.keys()):
                term = n['biosample_term_name']
                print ("%s (%s) (%s)")%(term, n['assay_term_name'],n['accession'])
                a = Ontology.Ontology().search(term, True, True)
                print "====="




# ROADMAP
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.biomics
experiments = list(db.roadmap.find())

for idx, n in enumerate(experiments):
        term = n['Sample Name']
        a = Ontology.Ontology().search(term, True, False)
        if len(a) == 1:
                db.roadmap.update({'_id': n['_id']}, {'$set': {'Ontology': a[0]['term_id'], 'Synonym': a[0]['synonym']}})




from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.biomics
experiments = list(db.encode.find())

for idx, n in enumerate(experiments):
        term = n['Sample Name']
        a = Ontology.Ontology().search(term, True, False)
        if len(a) == 1:
                db.roadmap.update({'_id': n['_id']}, {'$set': {'Ontology': a[0]['term_id'], 'Synonym': a[0]['synonym']}})





t = 0 #total
m = 0 #match
e = 0 #exact
f = 0 #fuzzy

for idx, n in enumerate(resp['@graph']):
        # time.sleep(1)
        if ('biosample_term_name' in n.keys()):
                term = n['biosample_term_name']
                print ("%s (%s) (%s)")%(term, n['assay_term_name'],n['accession'])
                a = []
                a = Ontology.Ontology().search(term, True, False)
                if len(a):
                        m+=1
                        if len(a) == 1:
                                e+=1
                        else:
                                f+=1
                t += 1
                print "====="
                print ("%d/%d - exact: %d/%d - fuzzy: %d/%d - not found: %d/%d")%(m, t, e, t, f, t, (t-m), t)