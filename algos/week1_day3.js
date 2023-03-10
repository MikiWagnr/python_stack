const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
// function reverseString(str) {
//     newList = ''
//     for (var i = str.length-1; i>=0; i--){
//         newList+= str[i]
//     }
//     return newList
// }

function reverseString(str) {
    newList = []
    for (var i = str.length-1; i>=0; i--){
        newList.push(str[i])
    }
    return newList.join("")
}

console.log(reverseString(str1))
console.log(reverseString(str2))
console.log(reverseString(str3))
console.log(reverseString(str4))