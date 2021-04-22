#FROM ubuntu:latest

#RUN apt-get update && apt-get install -y strongswan libstrongswan libgmp-dev kmod && apt-get upgrade -y

FROM buildpack-deps:xenial

RUN apt-get update && apt-get install -y haveged libgmp-dev module-init-tools netcat && apt-get upgrade -y

ENV STRONGSWAN_VERSION 5.7.2

ADD https://download.strongswan.org/strongswan-$STRONGSWAN_VERSION.tar.gz /tmp/
RUN tar -zxvf /tmp/strongswan-$STRONGSWAN_VERSION.tar.gz -C /tmp/
RUN mv /tmp/strongswan-$STRONGSWAN_VERSION /tmp/strongswan
RUN cd /tmp/strongswan \
    && ./configure --prefix=/usr --sysconfdir=/etc \
	    --enable-aesni \
	    --enable-gcm \
	    --enable-sql \
	    --enable-mysql \
	    --enable-sqlite \
			&& make \
			&& make install \
			&& rm -rf "/tmp/strongswan*"
ADD config_ssl.sh /etc/config_ssl.sh
ADD generate-mobileconf.py /etc/generate-mobileconf.py
# ADD ipsec.conf /etc/ipsec.conf
# ADD ipsec.secrets /etc/ipsec.secrets
# ADD strongswan.conf /etc/strongswan.conf
# ADD ./cacerts /etc/ipsec.d/cacerts
# ADD ./certs /etc/ipsec.d/certs
# ADD ./private /etc/ipsec.d/private
EXPOSE 4500/udp 500/udp
CMD ipsec start --nofork
