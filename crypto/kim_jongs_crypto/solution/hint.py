#!/usr/bin/env python3

ciphertext = '''
45--69-113--89-48--46-85--77-68--44-97--65-112--74-113--89-112--80-116--84-48--4
6-68--28-101--77-112--104-68--46-48--14-112--82-116--76-96--94-65--33-101--77-11
2--82-101--69-97--89-65--41-116--114-81--81-64--66-69--69-84--84-84--84-69--67-8
0--74-65--39-100--94-81--47-101--79-117--117-68--26-101--101-68--36-101--79-116-
-114-64--32-112--82-117--85-116--84-101--99-68--28-101--77-112--80-97--67-101--1
01-84--44-96--64-97--71-113--75-48--14-36-
'''

# Split the ciphertext into chunks, one chunk per encrypted character.
chunks = ciphertext.replace('\n', '').split('--')

# Remove the dashes, leaving us with one or two numerical strings per character.
strarrays = [chunk.strip('-').split('-') for chunk in chunks]

# Convert the numerical strings to actual numbers for easier processing.
numarrays = [[int(s) for s in strarray] for strarray in strarrays]

# Last parsing step: the double dashes are actually a dash and a minus sign.
numarrays = [numarrays[0]] + [[-a[0], a[1]] for a in numarrays[1:]]

plaintext = ''
success = False

# Assume the first plaintext character could have by any printable ASCII char.
for first in range(32, 127):

    # Check if the first character could have been this character.
    if False: #TODO ADD LOGIC HERE
        previous = first
        success = True
        plaintext = chr(first)

        print(plaintext)

        # If we have a match, go over the rest of the ciphertext.
        for numbers in numarrays[1:]:
            match_found = False

            # Again assume printable ASCII for the plaintext.
            for current in range(32, 127):

                # Check whether the current char could have been this char.
                test1 = False #TODO ADD LOGIC HERE
                test2 = False #TODO ADD LOGIC HERE

                # If we found a match, move to the next character.
                if test1 and test2:
                    match_found = True
                    previous = current

                    break

            if match_found:
                # If a new character is found is found, add it to the plaintext.
                plaintext += chr(current)

                print(plaintext)
            else:
                # If no match is found, restart with a new first character.
                success = False

                break
        
        if success:
            break
        
if success:
    print(f'Plaintext found: "{plaintext}"')
else:
    print('Could not decrypt ciphertext.')