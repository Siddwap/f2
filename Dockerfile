FROM debian:latest
RUN apt update && apt upgrade -y

RUN apt install git curl python3-pip ffmpeg -y

RUN pip3 install -U pip

RUN cd /

RUN git clone https://github.com/Siddwap/File2linkRailway

RUN cd File2linkRailway

WORKDIR /File2linkRailway

RUN pip3 install -U -r requirements.txt

CMD python3 PROCFILE
