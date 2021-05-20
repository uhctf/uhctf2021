const key = '138463';

const encUser = '8775a867ff01a739af31d769df6187198f9137c9bfc167f96ff197299f2147d9';
const encPass = '0940fe28f1bfbebec2d66aced266fa5ee2760a6ef2861afe0216aa0e12a63a9e';

const user = Decryption(encUser, key);
const pass = Decryption(encPass, key);

console.log('decrypted user: ' + user);
console.log('decrypted pass: ' + pass);

// Cleaned up encryption function, included for easy reference.
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

// Reverse of the encryption function.
function Decryption(strInput, strKey) {
    let strCode = '';
    let maskCode;
    let asciiCode;

    // Go backwards through the ciphertext, opposite to the encryption function.
    for (let i = strInput.length - 2; i >= 0; i -= 2) {

        // Parse the current hex byte from the ciphertext.
        maskCode = parseInt(strInput.substring(i, i + 2), 16);

        //TODO ADD LOGIC HERE

        // Go backwards through the key, opposite to the encryption function.
        for (let j = strKey.length - 1; j >= 0; j--) {

            // Get the current byte value.
            const asciiKey = strKey.charCodeAt(j);

            //TODO ADD LOGIC HERE
        }

        //TODO ADD LOGIC HERE

        // Prepend the decrypted character to the plaintext.
        strCode = String.fromCharCode(asciiCode) + strCode;
    }

    return strCode;
}