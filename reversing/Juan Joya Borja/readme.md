
# Juan Joya Borja

Creator: [Joris Herbots](https://github.com/JorisHerbots)

Flag 1 format: **uhctf{...}**

Flag 2 format: **custom**

## Description
**Juan Joya Borja** (5 April 1956 – 28 April 2021) was a Spanish comedian and actor known by the stage name **El Risitas**. To commemorate him, we created this beautiful website with one of his best clips. Some people report that the video doesn't work however...

## Hints flag 1
1. <details><summary>10%: Getting you on the right track.</summary>The video.mp4 is not what it pretends to be.</details>
2. <details><summary>50%: Technical description of what you're seeing.</summary>The video.mp4 is an XML file which represents an MPEG-DASH manifest. It contains a description of where to find all video and audio elements.</details>

## Hints flag 2
1. <details><summary>10%: Getting you on the right track.</summary>The video.mp4 file contains a very interesting reference.</details>
2. <details><summary>35%: Technical description.</summary>The video and audio tracks follow `ISO BMFF` formatting.A hex editor might be a handy tool on your quest of finding the flag.</details>
3. <details><summary>90%: Very helpful explanation</summary>The video tracks seems to be corrupt. The audio track however looks fine. When we compare these two, we clearly see that the fake flag does not belong, the four first bytes `00 00 00 1c` are missing, `iso5` should be preceded by `ftyp` and `iliketomoovit` is not a valid header.</details>

