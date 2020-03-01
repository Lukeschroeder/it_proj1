import sys
from networking import Client
infilename = 'PROJI-HNS.txt'





def main():
    args = sys.argv
    if len(args) != 4: print 'Insufficient Arguments'
    rsHostname = args[1]
    rsListenPort = int(args[2])
    tsListenPort = int(args[3])

    print 'RS Hostname:', rsHostname
    print 'RS Listen Port:', rsListenPort
    print 'TS Listen Port:', tsListenPort

    client = Client()
    client.connecttoserver(rsHostname, rsListenPort)
    client.close()
    



if __name__ == "__main__":
    main()