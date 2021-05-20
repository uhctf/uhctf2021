const user = 'admin';
const pass = 'wIZfG8ed';

const key = '138463';

const encUser = Encryption(user, key, 32);
const encPass = Encryption(pass, key, 32);

console.log('encrypted user: ' + encUser);
console.log('encrypted pass: ' + encPass);

const decUser = Decryption(encUser, key);
const decPass = Decryption(encPass, key);

console.log('decrypted user: ' + decUser);
console.log('decrypted pass: ' + decPass);

function Encryption(strInput, strKey, iSize) {
    let strCode = new Array;
    let maskCode = 0;
    let asciiCode;

    for (let i = 0; i < iSize; i++) {
        if (i < strInput.length) { asciiCode = strInput.charCodeAt(i); }
        else { asciiCode = 0; }

        if (i != 0) { asciiCode ^= maskCode; }

        for (let j = 0; j < (strKey.length); j++) {
            const asciiKey = strKey.charCodeAt(j);

            asciiCode = (asciiCode ^ asciiKey) - asciiKey;
        }

        maskCode = asciiCode & 0xFF;

        const hexCode = maskCode.toString(16);

        if (maskCode < 16) { strCode += '0'; }

        strCode += String(hexCode);
    }

    return strCode;
}

function Decryption(strInput, strKey) {
    let strCode = '';
    let maskCode;
    let asciiCode;

    for (let i = strInput.length - 2; i >= 0; i -= 2) {
        maskCode = parseInt(strInput.substring(i, i + 2), 16);
        asciiCode = maskCode;

        for (let j = strKey.length - 1; j >= 0; j--) {
            const asciiKey = strKey.charCodeAt(j);

            asciiCode = (asciiCode + asciiKey) ^ asciiKey;
        }

        if (i != 0) { asciiCode ^= parseInt(strInput.substring(i - 2, i), 16); }

        asciiCode &= 0xFF;

        strCode = String.fromCharCode(asciiCode) + strCode;
    }

    return strCode;
}