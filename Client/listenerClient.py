import sys
sys.path.insert(1, "../utility/")
import clientUtility as utils

def mainProg():
    hostIp, hostPort = utils.inputAddr()
    listenerId = utils.inputListener()
    cliSock = utils.makeConn(hostIp, hostPort)
    try:
        utils.listen(cliSock, listenerId)
        utils.closeConn(cliSock)
    except KeyboardInterrupt:
        utils.closeConn(cliSock)

if __name__ == '__main__':
    mainProg()