import sys
sys.path.insert(1, "../utility/")
import clientUtility as utils

def mainProg():
    hostIp, hostPort = utils.inputAddr()
    cliSock = utils.makeConn(hostIp, hostPort)
    utils.sendMsg(cliSock)
    utils.closeConn(cliSock)

if __name__ == '__main__':
    mainProg()