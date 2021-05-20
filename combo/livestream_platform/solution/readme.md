1. Go to the account recovery page (`/recover`) after logging in with password doesn't work
2. Use OSINT to find answers to security questions. The answers are:
    1. potvos.video (case insensitive)
    2. studio Oranjeboom (case insensitive)
    3. EDM-1.05a (case sensitive)
3. Go to the UHCTF livestream page (`/stream`)
4. Notice the livestream hasn't started yet, and the page echos back the time it is 'for you' (small nudge to timezones)
5. Notice your browser is sending a http-only cookie 'timezone' with `Europe/Brussels` in it
6. Change the cookie to a valid timezone where it is already past 20:00:00 (most likely `Japan` will work, but safest is `Etc/GMT-14`. Yes, that's a minus sign for a +14 timezone. Don't ask me, ask ISO.)
7. Access the video stream and notice the error about the "m3u8" file. The file can be found in de video tag or just use the network tab.
8. Copy the url of de m3u8 file and load it in VLC. Look through the video stream and find the flag
