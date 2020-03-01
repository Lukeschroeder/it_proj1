import sys
infilename = 'PROJI-DNSRS.txt'
DNStable = {}
TS_hostname = None
from networking import Server


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



def main():
    # print command line arguments
    args = sys.argv
    if len(args) != 2: print 'Insufficient Arguments'

    rsListenPort = int(args[1])
    populateDNStable()

    print 'TS Hostname:', TS_hostname
    print 'RS Listen Port:', rsListenPort

    server = Server(rsListenPort)
    server.accept()
    server.close()



        

if __name__ == "__main__":
    main()