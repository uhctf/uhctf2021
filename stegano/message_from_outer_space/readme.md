# Message from Outer Space

## Description
After 46 years of waiting, we have finally received our first message from extraterrestrial beings! These are exciting times for sure! We immediately put our brightest minds on the task of decoding this message. We were able to discover that the intelligent life forms are called the Semiprimes, but that's about it... We tried for weeks, but the message content itself has yet to be uncovered. Can you help us?

Flag format: **uhctf{...}**

Creator: [Joris Herbots](https://github.com/JorisHerbots)

## Attachments
* [message_from_outer_space.wav](https://drive.google.com/open?id=1hHrIn-_2O_Fr4EouRvYO05exO4TIBLEA)

## Hints
1. <details><summary>8%: Getting you on the right track.</summary>Anything rings a bell here https://en.wikipedia.org/wiki/Semiprime?</details>
2. <details><summary>25%: Clear task description, with technical advice.</summary>The sound file contains a series of large and small waves, which represent bits. You will need to extract the bits and lay them out in a bitmap, as described in https://en.wikipedia.org/wiki/Semiprime#Applications.  While there are multiple ways to do this, the Python wave module may be your best bet. You will need to do some scripting (or buy the next hint).</details>
3. <details><summary>67%: Very helpful script.</summary><a href="solution/waveform_to_binary.py">Link</a></details>