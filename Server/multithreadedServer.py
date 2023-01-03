import sys
sys.path.insert(1, "../utility/")
import serverUtility as utils

def mainProg():
    hostIp, hostPort = utils.inputAddr()
    srvSock = utils.serverInit(hostIp, hostPort)
    idx = 1
    sender_id = 1

    try:
        while True:
            conn, addr = utils.acceptConn(srvSock)
            conn.settimeout(5)
            sender_id = utils.identifySender(conn, addr)
            conn.settimeout(None)
            if sender_id != 0:
                utils.connAccount(idx, conn)
            else:
                utils.connAccount(sender_id, conn)
            idx += 1
            'Create thread for the newly connected client'
            thread = utils.Thread(target=utils.newClientSocketHandler, args=(conn, addr))
            thread.start()
            utils.log.debug(utils.connList)
    except KeyboardInterrupt:
        utils.serverClose(srvSock)

if __name__ == '__main__':
    mainProg()