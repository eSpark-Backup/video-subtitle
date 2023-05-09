#include <vlc/vlc.h>
#include <iostream>
#include <fstream>
#include <string>
#include <iostream>
#include <cstring>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include "srtparser.h"
#include <vector>
#include<chrono> 
#include<thread>

using namespace std;

int server_fd, new_socket, valread;
char buffer[1024];
struct sockaddr_in address;
int opt = 1;
int addrlen = sizeof(address);
int clientsArray[1] = { };

struct myString{
  std::string str1, str2;
};


void setClients(){

  if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen)) < 0) {
    perror("accept");
    exit(EXIT_FAILURE);
  }

  valread = read(new_socket, buffer, 1024);

  if (buffer[0] == '1'){
    clientsArray[0] = new_socket;
  }
  else if (buffer[0] == '2')
  {
    clientsArray[1] = new_socket;
  }

}

myString stringOperation(string str){

    myString s;
    string str2;
    vector<string> v;
    stringstream ss(str);
    while (getline(ss, str2, ' ')) {
      v.push_back(str2);
    }

    if (v.size()%2 != 0 ){
        v.push_back(" ");
    }

    vector<string> v1 (v.begin(), (v.begin() + v.size()/2));
    vector<string> v2 ((v.begin() + v.size()/2), v.end());
    for(auto& it:v1){
    s.str1+=" ";
    s.str1+=it;
    
    }
    for(auto& it:v2){
    s.str2+=it;
    s.str2+=" ";
    }
    
    return s;
    
}


// int main() {

//   SubtitleParserFactory *subParserFactory = new SubtitleParserFactory("Windfall.srt");
//   SubtitleParser *parser = subParserFactory->getParser();
//   std::vector<SubtitleItem*> sub = parser->getSubtitles();
//   int length = sub.size();
  

//   // Creating socket file descriptor
//   if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
//     perror("socket failed");
//     exit(EXIT_FAILURE);
//   }

//   // Forcefully attaching socket to the port 8080
//   if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt))) {
//     perror("setsockopt");
//     exit(EXIT_FAILURE);
//   }
  
//   address.sin_family = AF_INET;
//   address.sin_addr.s_addr = INADDR_ANY;
//   address.sin_port = htons(8080);

//   // Forcefully attaching socket to the port 8080
//   if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
//     perror("bind failed");
//     exit(EXIT_FAILURE);
//   }

//   if (listen(server_fd, 2) < 0) {
//     perror("listen");
//     exit(EXIT_FAILURE);
//   }

//   for (int i : clientsArray){
//     setClients();
//   }

// while (1) {
//     for (int i=0; i<=length; i++){  
//         auto my_str = sub[i]->getText();
//         my_str.erase(remove(my_str.begin(), my_str.end(), '-'), my_str.end());
//         myString result = stringOperation(my_str);
//         int timeDelay = (sub[i]->getEndTime() - sub[i]->getStartTime());
//         // send(clientsArray[0], result.str1.c_str(), strlen(my_str.c_str()), 0);
//         send(clientsArray[0], "THE", strlen("THE"), 0);
//         send(clientsArray[1], "THE", strlen("THE"), 0);
//         // send(clientsArray[1], result.str2.c_str(), strlen(my_str.c_str()), 0);
//         std::this_thread::sleep_for(std::chrono::milliseconds(timeDelay));
//     }
//     send(clientsArray[0], "THE", strlen("THE"), 0);
//     send(clientsArray[1], "END", strlen("END"), 0);
//     break;
// }

// close(server_fd);
//   return 0;
// }


int main(int argc, char* argv[]) {

    SubtitleParserFactory *subParserFactory = new SubtitleParserFactory("<srt file path>");
    SubtitleParser *parser = subParserFactory->getParser();
    std::vector<SubtitleItem*> sub = parser->getSubtitles();
    int length = sub.size();

      // Creating socket file descriptor
  if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
    perror("socket failed");
    exit(EXIT_FAILURE);
  }

  // Forcefully attaching socket to the port 8080
  if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt))) {
    perror("setsockopt");
    exit(EXIT_FAILURE);
  }
  
  address.sin_family = AF_INET;
  address.sin_addr.s_addr = INADDR_ANY;
  address.sin_port = htons(8080);

  // Forcefully attaching socket to the port 8080
  if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
    perror("bind failed");
    exit(EXIT_FAILURE);
  }

  if (listen(server_fd, 1) < 0) {
    perror("listen");
    exit(EXIT_FAILURE);
  }

  for (int i : clientsArray){
    setClients();
  }

    // create a new instance of the VLC player
    libvlc_instance_t* instance = libvlc_new(argc, argv);

    // create a new media instance with a subtitle file
    libvlc_media_t* media = libvlc_media_new_path(instance, "<video file path>");
    // libvlc_media_add_option(media, "sub-file=my_subtitles.srt");

    // create a new media player instance
    libvlc_media_player_t* player = libvlc_media_player_new_from_media(media);

    // set the media instance to the player
    libvlc_media_player_set_media(player, media);

    // play the media
    libvlc_media_player_play(player);

    // read subtitle file content and display in marquee
    // std::ifstream subtitle_file("my_subtitles.srt");
    // if (subtitle_file) {
        std::string subtitle_content = " ";
        libvlc_video_set_marquee_int(player, 0, 1);
        libvlc_video_set_marquee_string(player, 1, subtitle_content.c_str());
        libvlc_video_set_marquee_int(player, 7, 0);
        libvlc_video_set_marquee_int(player, 4, 4);
    // }
    libvlc_set_fullscreen(player, true);
    auto now = std::chrono::system_clock::now();

    // Get the duration since the epoch
    auto startVideo = now.time_since_epoch();

    // // Convert the duration to milliseconds
    auto millis = std::chrono::duration_cast<std::chrono::milliseconds>(startVideo);

    // // Get the value of the milliseconds count
    // auto millis_count = millis.count();
    
    // wait for the media to finish playing
    int i=0;
    libvlc_state_t state = libvlc_media_player_get_state(player);
    while (state != libvlc_Ended) {
        state = libvlc_media_player_get_state(player);
        auto now = std::chrono::system_clock::now();

        // Get the duration since the epoch
        auto currentTime = now.time_since_epoch();
        auto milliss = std::chrono::duration_cast<std::chrono::milliseconds>(currentTime);
        auto timeDiff = milliss - millis;
        // for (int i=0; i<=length; i++){  
        auto my_str = sub[i]->getText();
        // my_str.erase(remove(my_str.begin(), my_str.end(), '-'), my_str.end());
        // myString result = stringOperation(my_str);
        int timeDelay = (sub[i]->getEndTime() - sub[i]->getStartTime());
        
        if (sub[i]->getStartTime() <=  timeDiff.count()){
          if (timeDiff.count() > 30000){
            libvlc_video_set_marquee_int(player, 0, 0);
          }

            libvlc_video_set_marquee_string(player, 1, my_str.c_str());
            send(clientsArray[0], my_str.c_str(), strlen(my_str.c_str()), 0);
        // send(clientsArray[0], result.str1.c_str(), strlen(my_str.c_str()), 0);
        // send(clientsArray[0], "THE", strlen("THE"), 0);
        // send(clientsArray[1], "THE", strlen("THE"), 0);
        // send(clientsArray[1], result.str2.c_str(), strlen(my_str.c_str()), 0);
            std::this_thread::sleep_for(std::chrono::milliseconds(timeDelay));
            my_str = "       ";
            libvlc_video_set_marquee_string(player, 1, my_str.c_str());
            send(clientsArray[0], my_str.c_str(), strlen(my_str.c_str()), 0);
          
          // else{

          //   send(clientsArray[0], my_str.c_str(), strlen(my_str.c_str()), 0);
          //   std::this_thread::sleep_for(std::chrono::milliseconds(timeDelay));
          //   my_str = "";
          //   send(clientsArray[0], my_str.c_str(), strlen(my_str.c_str()), 0);

          // }

        if ( i <= length){
            i++;
        }
        else{

          send(clientsArray[0], "THE END", strlen("THE END"), 0);

        }
        }

    // }
    }

    // release the media player resources
    libvlc_media_player_release(player);
    libvlc_media_release(media);
    libvlc_release(instance);
    close(server_fd);

    return 0;
}
