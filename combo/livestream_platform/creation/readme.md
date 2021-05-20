A challenge to honour [Tim Vervoort](https://timvervoort.com) from [Potvos](https://potvos.video) for letting us stream our prize ceremony from their professional livestream studio 'Studio Oranjeboom'. Tim is an EDM researcher and founder of Potvos.

The challenge constists of three parts:

- OSINT (questions about Potvos and Tim)
- Websec (cookie based access control)
- Stegano (web streaming file)

The 'UHCTF Livestream Platform' is Potvos themed.

Stream is generated using following ffmpeg command:
```ffmpeg -y -i UHCTF.mp4 \
  -preset slow -g 48 -sc_threshold 0 \
  -map 0:0 -map 0:1 -map 0:0 -map 0:1 \
  -s:v:0 640x360 -c:v:0 libx264 -b:v:0 365k \
  -s:v:1 960x540 -c:v:1 libx264 -b:v:1 2000k  \
  -c:a copy \
  -var_stream_map "v:0,a:0 v:1,a:1" \
  -master_pl_name master.m3u8 \
  -f hls -hls_time 6 -hls_list_size 0 \
  -hls_segment_filename "v%v/segment%d.ts" \
  v%v/playlist.m3u8```
