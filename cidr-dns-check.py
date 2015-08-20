## This file is governed by The MIT License
## Created by Adam Thompson
## 20th August 2015

import socket
from netaddr import IPNetwork

rawFile = '/path/to/file'
DNSRecords = '/path/to/file'

## This boolean value outlines whether you want to see failures in
## the DNS Records file
DNSRecordsAndFailures = True

## This def pulls all the IP/Subnet content from the raw file
def getrawCIDR(rawFile):
	rawIPListFile = open(rawFile,'r')
	rawIPs = rawIPListFile.readlines()
	rawIPListFile.close()
	return rawIPs

##Get Full list of IPs from CIDR Notation
def getIPList(rawIPs):
	listOfIPs = []
	## Loop for ever CIDR Address
	for everyCIDR in rawIPs:
		## IPNetwork contains a list of every IP within a CIDR notation
		for individualIP in IPNetwork(everyCIDR):
			listOfIPs.append('%s' % individualIP) ## Append string to List
	return listOfIPs

## getDNSRecords uses a final output file, the list of IP's and a boolean to
## understand if you want to see failures in the output file, else it will
## print them to console
def getDNSRecord(DNSRecordsFile,listOfIPs,hostAndFailures):
	finalDNSList = open(DNSRecordsFile,'a')
	for ip in listOfIPs:
		##Try obtain DNS Record
		try:
			dns =  str(socket.gethostbyaddr(ip))
			finalDNSList.write(dns + "\n")
		## Catch Exceptions
		except socket.herror:
			if hostAndFailures:
				finalDNSList.write(ip + ", No DNS Record Found\n")
			else:
				print ip + ", No DNS Record Found"
		except socket.gaierror:
			if hostAndFailures:
				finalDNSList.write(ip + ", No DNS Record Found\n")
			else:
				print ip + ", No DNS Record Found"
	finalDNSList.close()

def main():
	rawIPs = getrawCIDR(rawFile)
	listOfIPs = getIPList(rawIPs)
	getDNSRecord(DNSRecords,listOfIPs,DNSRecordsAndFailures)

if __name__ == "__main__": main()