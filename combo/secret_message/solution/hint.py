def is_vowel(ch: str) -> bool:
    return ch in "aeuio"

def decode(enc: str) -> str:
    out = ""
    i = 0
    while i < len(enc):
        if enc[i] in " \n\t":
            out += enc[i]
            i += 1
        elif False: #TODO ADD LOGIC HERE
            out += enc[i]
            i += 3
        elif is_vowel(enc[i]):
            out += enc[i]
            i += 1
        else:
            raise ValueError("Not a valid code for", enc[i], enc[i-4:i+4])
    return out

print(decode(open("blomkvist.txt").read()))