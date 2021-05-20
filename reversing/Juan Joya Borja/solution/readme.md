
1. When the website is opened, one shall encounter a non-working video element. Looking at the source reveils a video.mp4 file.
2. The video.mp4 file is in actuality an MPEG-DASH manifest (MPD). The first flag is hidden inside the nested structure. Quick manual look or a strings & grep combination quickly reveals it.
3. The manifest root element contains a non-standard attribute called `oldManifestLocation` which points to the still existing original MPD.
4. Two possible ways forward from here:
	4.1 Use youtube-dl to download the contents, by default an auto-merge is attempted which fails because of issues with the video track.
	4.2 The original MPD contains a comment pointing to an available archive which contains the mpds, init segments and raw video/audio segments (VLC is capabable of playing locally stored MPDs).
5. Playback with a capable video player (e.g., VLC) will reveal only an audio track which works fine.
6. When inspecting the init segment of the video track with a hex-viewer (e.g., Bless), a fake uhctf flag will be visible in the first bytes hinting at the ISO BMFF specification.
7. [Hard step] Read into ISO BMFF specification and discover the following
	- The fake flag needs to be deleted
	- The first 4 bytes need to be restored to `00 00 00 1c`
	- `iso5` should be preceded by `ftyp`
	- `iliketomoovit` should become `moov`
	- Alternative easier solution: Copy the initial structure over from the init segment belonging to the audio track `init1.m4s`
8. The video track has been repaired and is now playable
	8.1 In case youtube-dl was used, a merge of the video and audio tracks need to happen`ffmpeg -i <videofile> -i <audiofile> -c:v copy -c:a aac output.mp4` to be able to enjoy the video
9. Final key is hidden in the hardcoded subtitles (the `uhctf{` and closing bracket `}` are missing because these are interpreted as SRT formatting)

