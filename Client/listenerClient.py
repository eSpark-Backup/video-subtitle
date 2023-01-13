import sys
sys.path.insert(1, "../utility/")
import clientUtility as utils

def mainProg():
    hostIp, hostPort = utils.inputAddr()
    listenerId = utils.inputListener()
    cliSock = utils.makeConn(hostIp, hostPort)
    utils.sendIdentity(cliSock, listenerId)
    utils.getConfig(cliSock)
    window, msgLen, textLabel = utils.setupUi()
    window.update()

    try:
        utils.listen(cliSock, msgLen, window, textLabel)
        utils.closeConn(cliSock)
    except KeyboardInterrupt:
        utils.closeConn(cliSock)

if __name__ == '__main__':
    mainProg()
