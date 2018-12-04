FROM debian:stretch

MAINTAINER Sowlene

RUN apt-get update && apt-get upgrade -qy && apt-get install -qy \
	git \
	python3-tk
RUN apt-get -qy install python3-pip 
RUN pip3 install pygame
RUN git clone https://github.com/Sowlene/Drarrow.git
RUN pwd && ls && cd Drarrow && pwd &&  python3 Drarrow_base.py
