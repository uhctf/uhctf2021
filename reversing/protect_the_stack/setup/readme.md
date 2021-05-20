# Instructions

You can edit the used ports in the commands and dockerfile to your
liking.

```bash
gcc -g -O0 protectthestack.c -o protectthestack -fno-stack-protector
docker build -t protectthestack .
docker run -d --name=protectthestack -p 0.0.0.0:2200:31337 protectthestack
```

