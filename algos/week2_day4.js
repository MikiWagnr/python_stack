/* 
Parens Valid
Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

// const str1 = "Y(3(p)p(3)r)s";
// const expected1 = true;

// const str2 = "N(0(p)3";
// const expected2 = false;
// Explanation: not every parenthesis is closed.

// const str3 = "N(0)t ) 0(k";
// const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
// function parensValid(str) {
//     // implement a stack data structure
//     var stack = []
//     //scan for close bracket and checking if theres an opening bracket in the stack
//     for (var i = 0 ; i < str.length ; i++){
//         if (str[i] ===  '('){
//             stack.push(str[i])
//         }else if( str[i] === ')'){
//             //check if stack isnt empty
//             if (stack.length === 0){
//                 return false
//             }
//             //else pop last value
//             stack.pop()
//         }
//     }
//     /* if now match in stack return true*/
//     return stack.length === 0
// }

// console.log(parensValid(str1))
// console.log(parensValid(str2))
// console.log(parensValid(str3))
// console.log(parensValid(str4))

/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected1 = true;

const str2 = "D(i{a}l[ t]o)n{e";
const expected2 = false;

const str3 = "A(1)s[O (n]0{t) 0}k";
const expected3 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */

function bracesValid(str) {
    // implement a stack data structure
    var stack = [];
    // go through string and for every close bracket make sure there is an opening bracket in the stack
    for (var i = 0; i < str.length; i++) {
        if (str[i] === "(" || str[i] === "{" || str[i] === "[") {
            stack.push(str[i]);
        } else if (str[i] === ")" || str[i] === "}" || str[i] === "]") {
            // check if stack isn't empty 
            if (stack.length === 0) {
                return false;
            } else if (str[i] === ")" && stack[stack.length - 1] !== "(") {
                return false;
            } else if (str[i] === "}" && stack[stack.length - 1] !== "{") {
                return false;
            } else if (str[i] === "]" && stack[stack.length - 1] !== "[") {
                return false;
            }
            stack.pop();
            // else pop() last value
        }
    }
    // return if stack is empty
    return stack.length === 0;
}


function validateClose(stack, end){
    switch(end) {
        case ')':
            return stack[stack.length - 1] === '('
        case '}':
            return stack[stack.length - 1] === '{'
        case '}':
            re
    }
}

console.log(bracesValid(str1))
console.log(bracesValid(str2))
console.log(bracesValid(str3))

// function bracesValid(input){
//     count1 = 0
//     for(i=0;i<input.length;i++){
//         if(input[i] === '(' || input[i] === '[' || input[i] === '{'){
//             count1 += 1
//         }
//         else if(input[i] === ')' || input[i] === ']' || input[i] === '}'){
//             if(count1<=0){
//                 return false
//             }
//             else{
//                 count1 -= 1
//             }
//         }
//     }
//     console.log(count1 + "is")
//     if(count1 === 0){
//         return true
//     }
//     else{
//         return false
//     }
// }

