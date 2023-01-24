#include <iostream>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <unistd.h>

#define LOCAL_HOST "127.0.0.1"
#define PORT 8080
 
int main()
{
    int sock, clientFD;
    struct sockaddr_in serverAddr;
    char buffer[1024] = { 0 };

    /* ---------- ESTABLISHING SOCKET CONNECTION ----------*/
    /* --------------- socket() function ------------------*/
    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) 
    {
        std::cout << "Error Establishing Socket..." << std::endl;
        exit(1);
    }
 
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = inet_addr(LOCAL_HOST);
    serverAddr.sin_port = htons(PORT);

    /* ---------- CONNECTING CLIENT SOCKET TO SERVER SOCKET ----------*/
    /* --------------- connect() function ------------------*/
    clientFD = connect(sock, (struct sockaddr*)&serverAddr, sizeof(serverAddr));
    if (clientFD < 0) 
    {
        std::cout << "Connect Failed" << std::endl;
        exit(1);
    }

    /* ------------- Client Receiving Message Streams ------------- */
    do
    {
        read(sock, buffer, 1024);
        std::cout << buffer << std::endl;
    } while (*buffer != '*');
 
    // closing the connected socket
    close(clientFD);
    return 0;
}