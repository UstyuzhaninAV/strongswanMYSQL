#!/bin/bash
file="testuser@vpn.holacode.tech.mobileconfig"
openssl smime \
    -sign \
    -signer /etc/ipsec.d/cacerts/certificate.pem \
    -inkey /etc/ipsec.d/private/key.pem \
    -certfile /etc/ipsec.d/cacerts/ca.pem \
    -nodetach \
    -outform der \
    -in ${file} \
    -out sign-${file}
