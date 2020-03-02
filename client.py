import sys
from networking import Client
infilename = 'PROJI-HNS.txt'
outfilename = 'RESOLVED.txt'
datalength = 200
rsListenPort = None
tsListenPort = None
rsHostname = None


def queryHostNames(rsclient, tsclient):
    global rsListenPort
    global tsListenPort
    global rsHostname

    # Open file of hostnames to query
    infile = open(infilename, 'r')
    outfile = open(outfilename, 'w+')
    lines = infile.readlines()
    rsclient.connecttoserver(rsHostname, rsListenPort)
    connected = False

    for index in range(len(lines)):
        hostname = lines[index].strip()
        request = hostname.lower().encode('utf-8')
        print '[C]: RS request: ', request
        rsclient.socket.send(request)
        response = rsclient.socket.recv(datalength).decode('utf-8')
        DNSentry = response.split()
        
        if DNSentry[2] == 'A':
            print '[C]: RS response:', response
            if index != len(lines) - 1:
                outfile.write(response + '\n')
            else:
                outfile.write(response)
        elif DNSentry[2] == 'NS':
            print '[C]: RS response:', response
            print '[C]: TS request: ', request
            if connected == False:
                tsclient.connecttoserver(DNSentry[0].strip(), tsListenPort)
                connected = True
            tsclient.socket.send(request)
            response = tsclient.socket.recv(datalength).decode('utf-8')
            print '[C]: TS response:', response
            if index != len(lines) - 1:
                outfile.write(response + '\n')
            else:
                outfile.write(response)
            

    rsclient.close()



def main():
    args = sys.argv
    if len(args) != 4: print 'Insufficient Arguments'

    global rsHostname
    global rsListenPort
    global tsListenPort

    rsHostname = args[1]
    rsListenPort = int(args[2])
    tsListenPort = int(args[3])

    rsclient = Client()
    tsclient = Client()
    queryHostNames(rsclient, tsclient)




if __name__ == "__main__":
    main()
