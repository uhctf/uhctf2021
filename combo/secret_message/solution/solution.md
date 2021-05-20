# Secret Message

Creator: [Bas Van Assche](https://github.com/basva923)

> We managed to intercept a message between two terrorist groups. Can you help to find the hidden message?

## Attachments
- Encrypted message

## Solution
The first method to solve this challenge is to look closely to the file. There are a lot of o's in the file. Every non vowel character is duplicated and an 'o' is put in the middle.

> The word 'test' for example is translated to 'totesostot'.

The second method is to look at the filename: 'Blomkvist'. The charakter 'Blomkvist' or 'Kalle Blomkvist' was created by writer Astrid Lindgren. The code is explained in one of her [books](https://books.google.be/books?id=Dq4vDwAAQBAJ&lpg=PT21&ots=YYjWv3SBYo&dq=kalle%20blomkvist%20code&hl=nl&pg=PT21#v=onepage&q=kalle%20blomkvist%20code&f=false).

All that is left now is to create a python script to decode the message and to find the flag:

```python
def is_vowel(ch: str) -> bool:
    return ch in "aeuio"

def decode(enc: str) -> str:
    out = ""
    i = 0
    while i < len(enc):
        if enc[i] in " \n\t":
            out += enc[i]
            i += 1
        elif not is_vowel(enc[i]) and enc[i+1] == "o" and enc[i] == enc[i+2]:
            out += enc[i]
            i += 3
        elif is_vowel(enc[i]):
            out += enc[i]
            i += 1
        else:
            raise ValueError("Not a valid code for", enc[i], enc[i-4:i+4])
    return out

print(decode(open("blomkvist.txt").read()))
```
