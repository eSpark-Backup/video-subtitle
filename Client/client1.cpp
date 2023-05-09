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
#include <vector>
#include <chrono> 
#include <sstream>

using namespace std;

#define PORT 8080
int sock = 0, valread, client_fd;
char buffer[1024];

std::string stringOperation(string str){

    string s, s1, str2;
    vector<std::string> v;
    std::stringstream ss(str);
    while (getline(ss, str2, ' ')) {
      v.push_back(str2);
    }

    if (v.size()%2 != 0 ){
        v.push_back(" ");
    }
	
	vector<string> v1 (v.begin(), (v.begin() + v.size()/2));
    vector<string> v2 ((v.begin() + v.size()/2), v.end());

	for(auto& it:v1){
    s+=it;
	s+=" ";
    }
	for(auto& it:v2){
    s1+=it;
	s1+=" ";
    }
	

								 
    return s + "\n" + s1;
    
}


void guiScreen(){

	Fl_Window *window = new Fl_Window(1280, 720, "Subtitle");
	window->color(FL_BLACK);
	window->fullscreen();
	Fl_Box *box = new Fl_Box(0, 0, window->w()-10, window->h()-10, " ");
	window->end();
	window->show();

	auto now = std::chrono::system_clock::now();
	// Get the duration since the epoch
	auto currentTime = now.time_since_epoch();
	auto millis = std::chrono::duration_cast<std::chrono::milliseconds>(currentTime);
	int i=3;
	while (window->shown()){
		valread = read(sock, buffer, 1024);
		auto now = std::chrono::system_clock::now();
		// Get the duration since the epoch
		auto currentTime = now.time_since_epoch();
		auto milliss = std::chrono::duration_cast<std::chrono::milliseconds>(currentTime);
		auto timeDiff = milliss-millis;
		std::string str(buffer);		
	
		if (i > 3 && str.size()>39){
			str = stringOperation(str);
		}
		box->label(str.c_str());
		
		if (timeDiff.count() < 60000 ){
			box->labelfont(FL_COURIER_ITALIC );
		}
		else if(timeDiff.count() >= 60000)
		{
			box->labelfont(FL_HELVETICA);
		}
		if (timeDiff.count() < 90000 ){
			box->labelsize(33);
		}else if(timeDiff.count() >= 90000 && timeDiff.count() < 120000){
			box->labelsize(33+i);
			i = i+2;
		}
		if (timeDiff.count() > 30000 && timeDiff.count() < 120000 ){
			box->labelcolor(FL_WHITE);
		}else if (timeDiff.count() > 120000 ){
			box->labelcolor(FL_DARK_YELLOW);
		}
		else if (timeDiff.count() < 30000 ){
			box->labelcolor(FL_BLACK);
		}
		box->align(FL_ALIGN_CENTER | FL_ALIGN_INSIDE);
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