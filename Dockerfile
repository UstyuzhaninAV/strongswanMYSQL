#FROM ubuntu:latest

#RUN apt-get update && apt-get install -y strongswan libstrongswan libgmp-dev kmod && apt-get upgrade -y

FROM buildpack-deps:buster

RUN apt-get update && apt-get install -y haveged libgmp-dev kmod netcat && apt-get upgrade -y \
    && rm -rf /var/lib/{apt,dpkg,cache,log}/ \
    && rm -rf /src/*.deb
ENV STRONGSWAN_VERSION 5.7.2

ADD https://download.strongswan.org/strongswan-$STRONGSWAN_VERSION.tar.gz /tmp/
RUN tar -zxvf /tmp/strongswan-$STRONGSWAN_VERSION.tar.gz -C /tmp/
RUN mv /tmp/strongswan-$STRONGSWAN_VERSION /tmp/strongswan
RUN cd /tmp/strongswan \
    && ./configure --prefix=/usr \
            --sysconfdir=/etc \
            --libexecdir=/usr/lib \
            --with-ipsecdir=/usr/lib/strongswan \
            --enable-aesni \
            --enable-chapoly \
            --enable-cmd \
            --enable-curl \
            --enable-dhcp \
            --enable-eap-dynamic \
            --enable-eap-identity \
            --enable-eap-md5 \
            --enable-eap-mschapv2 \
            --enable-eap-radius \
            --enable-eap-tls \
            --enable-farp \
            --enable-files \
            --enable-gcm \
            --enable-md4 \
            --enable-newhope \
            --enable-ntru \
            --enable-openssl \
            --enable-sha3 \
            --enable-shared \
            --disable-aes \
            --disable-des \
            --disable-gmp \
            --disable-hmac \
            --disable-ikev1 \
            --disable-md5 \
            --disable-rc2 \
            --disable-sha1 \
            --disable-sha2 \
            --disable-static \
      	    --enable-sql \
      	    --enable-mysql \
      	    --enable-sqlite \
			&& make \
			&& make install \
			&& rm -rf "/tmp/strongswan*"
EXPOSE 4500/udp 500/udp
ENTRYPOINT ["/usr/sbin/ipsec"]
CMD ["start", "--nofork"]
