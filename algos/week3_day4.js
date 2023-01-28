/* 
    Given a string,
    return a new string with the duplicates excluded
    Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

const str5 = "aabbccaa";
const expected5 = "abc";

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */

function stringDedupe(str) {
    var obj = {}
    var result = ''
    for (var i = 0; i < str.length; i ++){
        if ( !(str[i] in obj) ){
            obj[str[i]] = 1
        }
    }
    for (var key in obj){
        result += key
    }
    return result
}

// function stringDedupe(str) {
    
//     let a = str.length;
//     let res = " ";
//     for (let i = 0; i < a; i ++){
//         let j; j < a ; j++
//         for (j = i + 1; j < a ; j++)
//             if (str[i] == str[j])
//                 break;

//         if (j == a)
//             res == res + str[i];

//         }
//         return res;
// }

console.log(stringDedupe(str1));
console.log(stringDedupe(str2));
console.log(stringDedupe(str3));
console.log(stringDedupe(str4));
console.log(stringDedupe(str5));