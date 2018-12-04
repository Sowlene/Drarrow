FROM debian:stretch

MAINTAINER Sowlene

RUN apt-get update && apt-get upgrade -qy && apt-get install -qy \
	git \
	python3-tk \
	&& apt-get -qy install python3-pip \
	&& pip3 install pygame \
	&& git clone https://github.com/Sowlene/Drarrow.git \
	&& pwd && ls && cd Drarrow && pwd &&  python3 Drarrow_base.py
