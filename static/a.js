// console.clear();

$(document).ready(function(){
	var apikey = '249a37ae-d343-431c-86c6-82a429f9b954';
	var blacklist = ['CHEBI', 'Orphanet'];
	// var url = 'http://data.bioontology.org/search?q=';

	// var data = {
	// 							apikey: apikey,
	// 							q: query,
	// 							format: 'json',
	// 							ontologies: ontologies,
	// 							exact_match: false,
	// 	}
	// requestEBI;
	// keywords.onkeyup=function(){
	// 	bto.initialize(true);
	// };	



// var substringMatcher = function(strs) {
//   return function findMatches(q, cb) {
//     var matches, substringRegex;
 
//     // an array that will be populated with substring matches
//     matches = [];
 
//     // regex used to determine if a string contains the substring `q`
//     substrRegex = new RegExp(q, 'i');
 
//     // iterate through the pool of strings and for any string that
//     // contains the substring `q`, add it to the `matches` array
//     $.each(strs, function(i, str) {
//       if (substrRegex.test(str)) {
//         // the typeahead jQuery plugin expects suggestions to a
//         // JavaScript object, refer to typeahead docs for more info
//         matches.push({ value: str });
//       }
//     });
//  		console.log(matches);
//     cb(matches);
//   };
// };


// http://jsfiddle.net/Fresh/UkB7u/

	var onto = 'BTO';
	var bto = new Bloodhound({
		datumTokenizer: function (d) {
        return Bloodhound.tokenizers.whitespace(d.value);
    },
    queryTokenizer: Bloodhound.tokenizers.whitespace,
		name: 'bto-ontology',
		limit: 100,
		remote: {
        url: 'http://data.bioontology.org/search?q=%QUERY&format=json&exact_match=false&apikey=' + apikey + '&ontologies=' + onto,
        cache: true,

        filter: function (terms) {
        	return $.map(terms.collection, function (term) {
        		var tempOntology = term['@id'].split('/');
        		var ontologyId = tempOntology[tempOntology.length-1].split('_');

            if (blacklist.indexOf(ontologyId[0]) == -1) {
              return {
                  text: term.prefLabel,
                  definition: term.definition,
                  value: ontologyId
              };
            };
          });
        }
    },
	});

	var onto = 'EFO';
	var efo = new Bloodhound({
		datumTokenizer: function (d) {
        return Bloodhound.tokenizers.whitespace(d.value);
    },
    queryTokenizer: Bloodhound.tokenizers.whitespace,
		name: 'efo-ontology',
		limit: 100,
		remote: {
        url: 'http://data.bioontology.org/search?q=%QUERY&format=json&exact_match=false&apikey=' + apikey + '&ontologies=' + onto,
        cache: true,

        filter: function (terms) {
        	return $.map(terms.collection, function (term) {
        		var tempOntology = term['@id'].split('/');
        		var ontologyId = tempOntology[tempOntology.length-1].split('_');

        		if (blacklist.indexOf(ontologyId[0]) == -1) {
              return {
                  text: term.prefLabel,
                  definition: term.definition,
                  value: ontologyId
              };
            };
          });
        }
    },
	});
 
	bto.initialize();
	efo.initialize();


	$('input#keywords').tagsinput({
  	itemValue: 'value',
  	itemText: 'text'
	});

	$('input#keywords').tagsinput('input').typeahead({
		hint: true,
		highlight: true,
		minLength: 1
	},
	{
		name: 'bto-terms',
		displayKey: 'text',
	  valueKey: 'value',
	  source: bto.ttAdapter(),
	  templates: {
	  	header: '<h3 class="ontology-name">BTO</h3>'
	  }
	},
	{
		name: 'efo-terms',
		displayKey: 'text',
	  valueKey: 'value',
	  source: efo.ttAdapter(),
	  templates: {
	  	header: '<h3 class="ontology-name">EFO</h3>'
	  }
	}).bind('typeahead:selected', $.proxy(function (obj, datum) {
	  this.tagsinput('add', datum);
	  this.tagsinput('input').typeahead('setQuery', '');
	}, $('#keywords')));





	// function requestEBI(keyword, ontologyname){
	// 	ontologyname = typeof ontologyname == 'undefined' ? 'null' : ontologyname;
	// 	 return $.ajax({
	// 		url: "http://www.ebi.ac.uk/ontology-lookup/term.view",
	// 		type: "GET",
	// 		data: {'termname':"abc",
	// 					'ontologyname': ontologyname,
	// 					'obsolete':'false',
	// 					'q':'termautocomplete',
	// 					'_':''
	// 		},
	// 		success: onSuccess,
	// 		error: onError
	// 	});

	// 	function onSuccess(data, status, jqXHR) {
	// 		console.log($.xml2json(data).response.item);
	// 		// return($.xml2json(data).response.item);
	// 		updateTerms($.xml2json(data).response.item);
	// 	}

	// 	function onError(xhr, status, error) {
	// 	    alert("It didn't work!!!");
	// 	}
	// };



	function updateTerms(data) {
	$('#keywords').tagsinput({
  	itemValue: 'value',
  	itemText: 'name'
	});

	// Adding custom typeahead support using http://twitter.github.io/typeahead.js
	// $('#keywords').tagsinput('input').typeahead({
	// 	hint: true,
	// 	highlight: true,
	// 	minLength: 1
	// },
	// {
	// 	name: 'bto-terms',
	// 	displayKey: 'name',
	//   valueKey: 'value',
	//   source: bto.ttAdapter(),
	//   templates: {
	//   	header: '<h3 class="ontology-name">BTO</h3>'
	//   }
	// }).bind('typeahead:selected', $.proxy(function (obj, datum) {  
	//   this.tagsinput('add', datum);
	//   this.tagsinput('input').typeahead('setQuery', '');
	// }, $('#keywords')));

};


});


