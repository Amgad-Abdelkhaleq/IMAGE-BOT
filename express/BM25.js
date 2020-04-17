/* eslint no-console: 0 */
// Load wink-bm25-text-search
var bm25 = require( './wink-bm25-text-search' );
// Create search engine's instance
var engine = bm25();
// Load NLP utilities
var nlp = require( 'wink-nlp-utils' );
var docs = require( '../static/KB/output.json');
// Define preparatory task pipe!
var pipe = [
  nlp.string.lowerCase,
  nlp.string.tokenize0,
  nlp.tokens.removeWords,
  nlp.tokens.stem,
  nlp.tokens.propagateNegations
];
// Contains search query.
var query;

// Step I: Define config
// Only field weights are required in this example.
engine.defineConfig( { fldWeights: { body: 1 } } );
// Step II: Define PrepTasks pipe.
// Set up 'default' preparatory tasks i.e. for everything else
engine.definePrepTasks( pipe );

// Step III: Add Docs
// Add documents now...
docs.forEach( function ( doc, i ) {
  // Note, 'i' becomes the unique id for 'doc'
  engine.addDoc( doc, i );
} );

// Step IV: Consolidate
// Consolidate before searching
engine.consolidate();

module.exports={
find_ans: function get_answer(query){ // Load sample data (load any other JSON data instead of sample)
// All set, start searching!
// `results` is an array of [ doc-id, score ], sorted by 
var results = engine.search(query);
 // -> 1 entries found.
// results[ 0 ][ 0 ] i.e. the top result is:
try {
    return query+"<p>"+docs[ results[ 0 ][ 0 ] ].body+"<p>"+'Number answers found:'+results.length+"<p>";
} catch (error) {
    return "not found";
}

}  
};