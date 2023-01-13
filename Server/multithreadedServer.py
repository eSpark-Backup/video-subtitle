import sys
sys.path.insert(1, "../utility/")
import serverUtility as utils

def mainProg():
    hostIp, hostPort = utils.inputAddr()
    utils.getClients()
    utils.setupConfig()
    utils.getMsgLen()
    srvSock = utils.serverInit(hostIp, hostPort)
    
    try:
        while True:
            conn, addr = utils.acceptConn(srvSock)
            conn.settimeout(utils.SERVER_SOCK_TIMEOUT_SEC)
            listenerId = utils.identifylistener(conn, addr)
            conn.settimeout(None)
            
            if listenerId < 0:
                conn.settimeout(utils.SERVER_SOCK_TIMEOUT_SEC)
                sender_id = utils.identifySender(conn, addr)
                conn.settimeout(None)
                if sender_id < 0:
                    utils.connAccount(sender_id, conn)
                    idx = sender_id
            else:
                utils.connAccount(listenerId, conn)
                idx = listenerId
            
            'Create thread for the newly connected client'
            thread = utils.Thread(target=utils.newClientSocketHandler, args=(conn, addr, idx))
            thread.start()
            utils.log.debug(utils.connList)
    except KeyboardInterrupt:
        utils.serverClose(srvSock)

if __name__ == '__main__':
    mainProg()