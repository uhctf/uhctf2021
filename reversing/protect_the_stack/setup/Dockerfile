FROM debian:stable-slim
RUN apt update
RUN apt install ucspi-tcp -y
RUN apt install gcc -y

# based on https://anee.me/how-to-host-a-ctf-b644a1f15618

RUN adduser noob
COPY --chown=noob:noob protectthestack.c /protectthestack.c
WORKDIR /
RUN gcc -g -O0 protectthestack.c -o protectthestack -fno-stack-protector
EXPOSE 31337

USER noob
ENV CTFFLAG=1e56531f-a8fa-45aa-be51-8616bd7e1c61
ENV CTFPASSWD=S3CreTPW%<3
CMD tcpserver -t 50 -RHl0 0.0.0.0 31337 /protectthestack
