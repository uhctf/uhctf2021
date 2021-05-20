# Old-Timey Security

## Description
There are good ways to implement web authentication, and then there's whatever Panasonic was doing with their WJ-NV200 Network Disk Recorder. This device was released in 2010, and authentication happens entirely through the URL, rather than through cookies or HTTP headers. This has several horrible security implications, not least of which is, if you could snap a picture of someone's screen when they are logged in, you could copy the URL and take over their account. As if that's not bad enough, the WJ-NV200 implementation includes the username and password in the URL as well. They are both encrypted, but encryption only helps if it's used correctly.

You receive a photo of a victim's screen, with the URL repeated below to save you time. The flag for this challenge is the victim's password.

`/cgi-bin/ulogin.cgi?USER=8775a867ff01a739af31d769df6187198f9137c9bfc167f96ff197299f2147d9&PASS=0940fe28f1bfbebec2d66aced266fa5ee2760a6ef2861afe0216aa0e12a63a9e&KEY=138463&TEM...`

Below is a WJ-NV200 for you to play with. Don't waste your time attacking it, that's not the goal of this challenge. Instead, have a look at how the client-side authentication mechanism works (it's straightforward), and see if you can deduce how to decrypt the password in the URL above.

http://172.19.14.80

Flag format: **free-form**

Creator: [Reinaert Van de Cruys](https://github.com/reinaertvdc)

## Hints
1. <details><summary>15%: Precise task description, but without technical details.</summary>In <code>/cgi-bin/start.cgi</code>, you will see a function <code>Encryption(strInput, strKey, iSize)</code> that encrypts your username and password before it is placed in the URL. In the URL you received, there is the encrypted password, as well as the key, so if you can write a reverse function for <code>Encryption()</code>, this should let you recover the plaintext password.</details>
2. <details><summary>40%: Largely finished script that you need to complete.</summary><a href="solution/hint.js">This script</a> is missing only a few key pieces of logic.</details>