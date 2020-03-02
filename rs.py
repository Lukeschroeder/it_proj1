import sys
infilename = 'PROJI-DNSRS.txt'
DNStable = {}
TS_hostname = None
from networking import Server
datalength = 200


# Fills in DNS table with entries from file 
def populateDNStable():
    infile = open(infilename, 'r')
    lines = infile.readlines()
    for index in range(len(lines)):
        global TS_hostname
        DNSentry = lines[index].split()
        if DNSentry[2] == 'A':
            DNStable[DNSentry[0].lower()] = DNSentry
        else:
            TS_hostname = DNSentry[0]




def queryDNStable(server):
    while(True):
        # Receive message from client
        hostname = server.activesocket.recv(datalength)
        if len(hostname) == 0: break
        if DNStable.has_key(hostname):
            DNSentry = DNStable[hostname]
            response = DNSentry[0] + ' ' + DNSentry[1] + ' ' + DNSentry[2]
            server.activesocket.send(response.encode('utf-8'))
        else:
            response = TS_hostname + ' - NS'
            server.activesocket.send(response.encode('utf-8'))





def main():
    # print command line arguments
    args = sys.argv
    if len(args) != 2: print 'Insufficient Arguments'

    rsListenPort = int(args[1])
    populateDNStable()

    server = Server(rsListenPort)
    server.accept()
    queryDNStable(server)
    server.close()



if __name__ == "__main__":
    main()