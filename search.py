from SOAPpy import Types, WSDL

ols = WSDL.Proxy('http://www.ebi.ac.uk/ontology-lookup/OntologyQuery.wsdl')
# http://www.ebi.ac.uk/ontology-lookup/WSDLDocumentation.do
# methods

def s(obj):
	return Types.simplify(obj)

# olsQuery: Returns matching identifiers
# Description: This function queries one or all ontologies for a pattern and returns all identiﬁers/terms.
# Usage: olsQuery(pattern, ontologyName=None, exact=False)
# Arguments:
# 	pattern				A character used to query the OLS.
# 	ontologyName		Optional. A character with the name of a valid ontology name.
# 	exact				Require pattern to match term exactly. Default is FALSE.

def olsQuery(pattern, ontologyName=None, exact=False):
	# if ontologyName=None, exact=False
	if ontologyName is None and exact is False: 
		return s(ols.getPrefixedTermsByName(pattern, True))
	# if ontologyName!=None, exact=False
	if not (ontologyName is None) and exact is False:
		return s(ols.getTermsByName(pattern, ontologyName, True))
	# if exact=True
	return s(ols.getTermsByExactName(exactName=keyword, ontologyName=(ontologyName or 'null')))