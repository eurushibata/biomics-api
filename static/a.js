$(document).ready(function(){
	var a= updateTerm.success;
// console.log(a);
	keywords.onkeyup=function(){
		console.log(keywords.value);
	};	



var substringMatcher = function(strs) {
  return function findMatches(q, cb) {
    var matches, substringRegex;
 
    // an array that will be populated with substring matches
    matches = [];
 
    // regex used to determine if a string contains the substring `q`
    substrRegex = new RegExp(q, 'i');
 
    // iterate through the pool of strings and for any string that
    // contains the substring `q`, add it to the `matches` array
    $.each(strs, function(i, str) {
      if (substrRegex.test(str)) {
        // the typeahead jQuery plugin expects suggestions to a
        // JavaScript object, refer to typeahead docs for more info
        matches.push({ value: str });
      }
    });
 		console.log(matches);
    cb(matches);
  };
};
 


	var updateTerm = function(ontologyname='null'){
		// $.ajax({
		// 	url: "http://www.ebi.ac.uk/ontology-lookup/term.view",
		// 	type: "GET",
		// 	data: {'termname':'abc',
		// 				'ontologyname': ontologyname,
		// 				'obsolete':'false',
		// 				'q':'termautocomplete',
		// 				'_':''
		// 	},
		// 	success: onSuccess,
		// 	error: onError
		// });

		function onSuccess(data, status, jqXHR) {
			console.log($.xml2json(data).response);
			// return($.xml2json(data).response);
		}

		function onError(xhr, status, error) {
		    alert("It didn't work!!!");
		}
	};
	
	$('#input').tagsinput({
  	itemValue: 'value',
  	itemText: 'text'
	});
// $('#input').tagsinput('add', { "value": 1 , "text": "Amsterdam"   , "continent": "Europe"    });
// $('#input').tagsinput('add', { "value": 4 , "text": "Washington"  , "continent": "America"   });
// $('#input').tagsinput('add', { "value": 7 , "text": "Sydney"      , "continent": "Australia" });
// $('#input').tagsinput('add', { "value": 10, "text": "Beijing"     , "continent": "Asia"      });
// $('#input').tagsinput('add', { "value": 13, "text": "Cairo"       , "continent": "Africa"    });

var cities = [ { "value": 1 , "text": "Amsterdam"   , "continent": "Europe"    },
  { "value": 2 , "text": "London"      , "continent": "Europe"    },
  { "value": 3 , "text": "Paris"       , "continent": "Europe"    },
  { "value": 4 , "text": "Washington"  , "continent": "America"   },
  { "value": 5 , "text": "Mexico City" , "continent": "America"   },
  { "value": 6 , "text": "Buenos Aires", "continent": "America"   },
  { "value": 7 , "text": "Sydney"      , "continent": "Australia" },
  { "value": 8 , "text": "Wellington"  , "continent": "Australia" },
  { "value": 9 , "text": "Canberra"    , "continent": "Australia" },
  { "value": 10, "text": "Beijing"     , "continent": "Asia"      },
  { "value": 11, "text": "New Delhi"   , "continent": "Asia"      },
  { "value": 12, "text": "Kathmandu"   , "continent": "Asia"      },
  { "value": 13, "text": "Cairo"       , "continent": "Africa"    },
  { "value": 14, "text": "Cape Town"   , "continent": "Africa"    },
  { "value": 15, "text": "Kinshasa"    , "continent": "Africa"    }
];

// Adding custom typeahead support using http://twitter.github.io/typeahead.js
$('#input').tagsinput('input').typeahead({
  valueKey: 'text',
  local: cities,
  template: '<p>{{text}}</p>',
	engine: Hogan
}).bind('typeahead:selected', $.proxy(function (obj, datum) {  
  this.tagsinput('add', datum);
  this.tagsinput('input').typeahead('setQuery', '');
}, $('#input')));




});


