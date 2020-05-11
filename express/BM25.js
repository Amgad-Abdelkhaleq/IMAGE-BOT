module.exports={
  find_ans: function get_answer(query){ // Load sample data (load any other JSON data instead of sample)
/* eslint no-console: 0 */
// Load wink-bm25-text-search
var bm25 = require( './wink-bm25-text-search' );
// Create search engine's instance
var engine = bm25();
// Load NLP utilities
var nlp = require( 'wink-nlp-utils' );
var docs = require( '../static/KB/output.json');
console.log(docs)
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

// Step I: Define config and set doc priorty 
engine.defineConfig( { fldWeights: { body: 1 } } );
// Step II: Define PrepTasks pipe.
engine.definePrepTasks( pipe );
// Step III: Add Docs
docs.forEach( function ( doc, i ) {
  engine.addDoc( doc, i );
} );
// Step IV: Consolidate
// Consolidate before searching
engine.consolidate();

var results = engine.search(query);
try {
    //return answer to flask server for recived question if answer does not exist it will send not found   
    return {"Answer": docs[ results[ 0 ][ 0 ] ].body,"Number_answers_found":results.length,"image_name": docs[ results[ 0 ][ 0 ] ].image,"type":"QA"}
} catch (error) {
    return {"Answer":"not found","image_name":'',"type":"QA"};
}

}  
};