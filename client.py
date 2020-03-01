import sys
from networking import Client
infilename = 'PROJI-HNS.txt'
outfilename = 'RESOLVED.txt'
datalength = 200



def queryHostNames(client, rsHostname, rsListenPort, tsListenPort):
    # Connect to server 
    client.connecttoserver(rsHostname, rsListenPort)

    # Open file of hostnames to query
    infile = open(infilename, 'r')
    lines = infile.readlines()

    for index in range(len(lines)):
        hostname = lines[index].strip()
        client.socket.send(hostname.lower().encode('utf-8'))

    client.close()



def main():
    args = sys.argv
    if len(args) != 4: print 'Insufficient Arguments'
    rsHostname = args[1]
    rsListenPort = int(args[2])
    tsListenPort = int(args[3])

    client = Client()
    queryHostNames(client, rsHostname, rsListenPort, tsListenPort)


    



if __name__ == "__main__":
    main()