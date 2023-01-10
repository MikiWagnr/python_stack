/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

const str1 = "object oriented programming";
const expected1 = "OOP";
function acros(wordString) {
    var stringBreak = wordString.split(' ')
    var result = ''
    for (var i = 0; i < stringBreak.length; i++) {
        result += stringBreak[i][0].toUpperCase();
    }
    return result
}
console.log(acros(str1));

// The 4 pillars of OOP
const str2 = "abstraction polymorphism inheritance encapsulation";
const expected2 = "APIE";
console.log(acros(str2));
const str3 = "software development life cycle";
const expected3 = "SDLC";
console.log(acros(str3))
// Bonus: ignore extra spaces
const str4 = "  global   information tracker    ";
const expected4 = "GIT";

function acronymize(wordString) {
    var wordSplit = wordString.split(' ')
    var result = ''
    for (var i = 0; i < wordSplit.length; i++) {
        if (wordSplit[i] != '') {
            result += wordSplit[i][0].toUpperCase();
        }
    }
    return result
}
console.log(acronymize(str4))
/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * //@param {string} wordsStr A string to be turned into an acronym.
 * //@returns {string} The acronym.
 */
function acronymize(str) { }