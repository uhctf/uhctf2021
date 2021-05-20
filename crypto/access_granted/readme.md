# Access Granted

## Description
One of our intelligence officers managed to get hold of the original source code of an cipher algorithm developed by North Korea. They call it our supreme leader's perfect state-of-the-art encryption algorithm". Later that day, we also received intel of a message sent from Kim Jong Un to his friend Vlad.

Can you decipher the received ciphertext using the source code? You will be... royally rewarded.

Flag format: **UHCTF{...}**

Creator: [Mariano Di Martino](https://github.com/M-DiMartino)

## Attachments
* [UltraSecureKey_DevelopedByRUL_ForBachelorProject](UltraSecureKey_DevelopedByRUL_ForBachelorProject.cpp)

## Hints
1. <details><summary>17%: General advice on how to approach the problem.</summary>
    1. The code has poor formatting, and some parts are overly complicated or do nothing at all. Don't hesitate to clean up and simplify.<br/>
    2. Be sure to use a debugger to step through the code, or at least make sure you can build and run in a single click. Don't just read the code, try it, or you might waste time on minsunderstandings.<br/>
    3. The input values are all used in different ways. Some might be easier to pin down than others, maybe start with those.<br/>
    4. Once you understand the code, you will discover a small set of constaints on the input values, and the answer will be straightforward
    </details>
2. <details><summary>67%: Greatly simplifying the problem for you.</summary><code>
    part1 + part2 = 96<br/>
    part2 = part3<br/>
    part2 > 40<br/>
    part1 < part2 + part3<br/>
    part2 is divisible by 2, 3, 4, 6, 8, 12, 16<br/>
    part4 = 11 * (2 ^ 16) + 1504
    </code></details>