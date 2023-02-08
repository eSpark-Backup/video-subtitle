
#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#include <netdb.h>
#include <iostream>
#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Box.H>

#define PORT 8080
int sock = 0, valread, client_fd;
char buffer[1024];

void guiScreen(){

	Fl_Window *window = new Fl_Window(1920, 515, "Subtitle");
	window->color(FL_BLACK);
	// window->fullscreen();
	Fl_Box *box = new Fl_Box(0, 0, window->w()-10, window->h()-10, " ");
	window->end();
	window->show();

	while (window->shown()){
		valread = read(sock, buffer, 1024);
		box->label(buffer);
		box->labelfont(FL_HELVETICA);
		box->labelsize(60);
		box->labelcolor(FL_WHITE);
		box->align(FL_ALIGN_RIGHT | FL_ALIGN_INSIDE);
		box->redraw();
		Fl::check();
		memset(buffer, 0, sizeof(buffer));
		fflush(stdout);
		if (valread == 0){
			break;
		}
	}
	window->hide();  // hide the window
	delete window;
}

int main()
{
	struct sockaddr_in serv_addr;
	if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
		printf("\n Socket creation error \n");
		return -1;
	}

	struct hostent *host = gethostbyname("<serverhostname>.local");
	if (host == NULL) {
		perror("gethostbyname failed");
		exit(EXIT_FAILURE);
	}

	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(8080);
	serv_addr.sin_addr = *((struct in_addr *)host->h_addr);

	while ((client_fd
		= connect(sock, (struct sockaddr*)&serv_addr,
				sizeof(serv_addr)))
		< 0){}

	const char *data = "1";
    send(sock, data, strlen(data), 0);
	guiScreen();
	close(client_fd); // closing the connected socket
	return 0;
}
