// using the decimal.js library for the implementatino of function 
const Decimal = require('decimal.js');

function parseJsonfunc(jsonString) {
    return JSON.parse(jsonString, (key, value) => {
        if (typeof value === 'string') {
            // for parsing the BigInt if it is an Integer
            if (/^-?\d+$/.test(value)) {
                return BigInt(value);
            }
            // Attempt to parse as Decimal if it’s a float
            if (/^-?\d*\.\d+$/.test(value)) {
                return new Decimal(value);
            }
        }
        return value;
    });
}

//taking arbitrary large int and large float values for parseJsonfunc
const jsonString = '{"large_int": "123456789012345678901", "large_float": "12345.6789012345678901234567890"}';
const parsedJson = parseJsonfunc(jsonString);

console.log(parsedJson);