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
#define MSG "Hello From Server!"

int main()
{
    int sock, serverFD;
    struct sockaddr_in serverAddr;
    socklen_t serverSocLen = sizeof(serverAddr);
    char buffer[1024] = { 0 };
 
    /* ---------- ESTABLISHING SOCKET CONNECTION ----------*/
    /* --------------- socket() function ------------------*/
    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) 
    {
        std::cout << "Error Establishing Socket..." << std::endl;
        exit(1);
    }

    std::cout << "Socket Server Created..." << std::endl;

    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = inet_addr(LOCAL_HOST);
    serverAddr.sin_port = htons(PORT);
 
    /* ---------- BINDING THE SOCKET ---------- */
    /* ---------------- bind() ---------------- */
    if (bind(sock, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) < 0) 
    {
        std::cout << "Bind Failed" << std::endl;
        exit(1);
    }

    /* ------------- LISTENING CALL ------------- */
    /* ---------------- listen() ---------------- */
    if (listen(sock, 1) < 0) 
    {
        std::cout << "Listen Failed" << std::endl;
        exit(1);
    }

     /* ------------- ACCEPTING CLIENTS  ------------- */
    /* ----------------- accept() ------------------- */

    serverFD = accept(sock, (struct sockaddr*)&serverAddr, &serverSocLen);
    if (serverFD < 0) 
    {
        std::cout << "Accept Failed" << std::endl;
        exit(1);
    }

    /* ------------- Server Reading Message ------------- */
    read(serverFD, buffer, 1024);
    std::cout << buffer << std::endl;

    /* ------------- Server Sending Message------------- */
    send(serverFD, MSG, strlen(MSG), 0);
    std::cout << "Message Sent" << std::endl;
 
     /* ------------- Closing the Connected & Listerning Socket ------------- */
    close(serverFD);
    shutdown(sock, SHUT_RDWR);

    return 0;
}