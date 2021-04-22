#!/usr/bin/env python3
import sys
from string import Template
import uuid

if (len(sys.argv) < 4):
    print("Usage: generate.py {username} {password} {hostname}")
    exit(0)

username = sys.argv[1]
password = sys.argv[2]
hostname = sys.argv[3]

content = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>PayloadContent</key>
	<array>
		<dict>
			<key>IKEv2</key>
			<dict>
				<key>OnDemandEnabled</key>
                    <integer>1</integer>
                    <key>OnDemandRules</key>
				<array>
					<dict>
						<key>Action</key>
						<string>Connect</string>
					</dict>
				</array>
				<key>AuthName</key>
				<string>$username</string>
				<key>AuthPassword</key>
				<string>$password</string>
				<key>AuthenticationMethod</key>
				<string>None</string>
				<key>ChildSecurityAssociationParameters</key>
				<dict>
					<key>DiffieHellmanGroup</key>
					<integer>2</integer>
					<key>EncryptionAlgorithm</key>
					<string>AES-256</string>
					<key>IntegrityAlgorithm</key>
					<string>SHA1-96</string>
					<key>LifeTimeInMinutes</key>
					<integer>1440</integer>
				</dict>
				<key>DeadPeerDetectionRate</key>
				<string>Medium</string>
				<key>DisableMOBIKE</key>
				<integer>0</integer>
				<key>DisableRedirect</key>
				<integer>0</integer>
				<key>EnableCertificateRevocationCheck</key>
				<integer>0</integer>
				<key>EnablePFS</key>
				<integer>0</integer>
				<key>ExtendedAuthEnabled</key>
				<true/>
				<key>IKESecurityAssociationParameters</key>
				<dict>
					<key>DiffieHellmanGroup</key>
					<integer>2</integer>
					<key>EncryptionAlgorithm</key>
					<string>AES-256</string>
					<key>IntegrityAlgorithm</key>
					<string>SHA1-96</string>
					<key>LifeTimeInMinutes</key>
					<integer>1440</integer>
				</dict>
				<key>LocalIdentifier</key>
				<string>$username</string>
				<key>RemoteAddress</key>
				<string>$hostname</string>
				<key>RemoteIdentifier</key>
				<string>$hostname</string>
				<key>ServerCertificateCommonName</key>
				<string>$hostname</string>
				<key>ServerCertificateIssuerCommonName</key>
				<string>$hostname</string>
				<key>UseConfigurationAttributeInternalIPSubnet</key>
				<integer>0</integer>
			</dict>
			<key>IPv4</key>
			<dict>
				<key>OverridePrimary</key>
				<integer>0</integer>
			</dict>
			<key>PayloadDescription</key>
			<string>Configures VPN settings</string>
			<key>PayloadDisplayName</key>
			<string>VPN</string>
			<key>PayloadIdentifier</key>
			<string>com.apple.vpn.managed.$uuid1</string>
			<key>PayloadType</key>
			<string>com.apple.vpn.managed</string>
			<key>PayloadUUID</key>
			<string>$uuid1</string>
			<key>PayloadVersion</key>
			<integer>1</integer>
			<key>Proxies</key>
			<dict>
				<key>HTTPEnable</key>
				<integer>0</integer>
				<key>HTTPSEnable</key>
				<integer>0</integer>
			</dict>
			<key>UserDefinedName</key>
			<string>$hostname</string>
			<key>VPNType</key>
			<string>IKEv2</string>
		</dict>
	</array>
	<key>PayloadDisplayName</key>
	<string>$hostname</string>
	<key>PayloadIdentifier</key>
	<string>me.molchanoff.vpn</string>
	<key>PayloadRemovalDisallowed</key>
	<false/>
	<key>PayloadType</key>
	<string>Configuration</string>
	<key>PayloadUUID</key>
	<string>$uuid2</string>
	<key>PayloadVersion</key>
	<integer>1</integer>
</dict>
</plist>"""

template = Template(content)
values = {"username": username, "password": password, "hostname":hostname, "uuid1": uuid.uuid4(), "uuid2": uuid.uuid4()}
result = template.substitute(values)
out = open("{0}@{1}.mobileconfig".format(username, hostname), "w")
out.write(result)
out.close()