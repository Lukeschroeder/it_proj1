import sys
from networking import Server
infilename = 'PROJI-DNSTS.txt'
DNStable = {}



# Fills in DNS table with entries from file 
def populateDNStable():
    infile = open(infilename, 'r')
    lines = infile.readlines()
    for index in range(len(lines)):
        DNSentry = lines[index].split()
        DNStable[DNSentry[0].lower()] = DNSentry



def main():
    args = sys.argv
    if len(args) != 2: print 'Insufficient Arguments'

    tsListenPort = int(args[1])
    print 'TS Listen Port:', tsListenPort

    populateDNStable()
    server = Server(tsListenPort)
    server.accept()

    
   
        
if __name__ == "__main__":
    main()




