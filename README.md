Project Directories
===================

**Server:**  Contain server file.

**Client:**  Contain 1 client file.

**Library:**  Contain srt parser header file. Must be include in server file.

**FLTK:**  Contain fltk library zip file. Need to extract on system and build it for gui.

Setting FLTK library on linux for GUI
=====================================

**Install dependencies:** FLTK requires certain libraries and tools to be installed on your system, including X11 and Xext libraries, the X Window System, and the FreeType library.

    sudo apt-get update
    sudo apt-get install libfltk1.3-dev libx11-dev libxext-dev libxft-dev libxcursor-dev libxinerama-dev libgl1-mesa-dev

**Extract the source code:** Extract the FLTK source code archive to a directory of your choice.

**Configure and build FLTK:** Open a terminal, navigate to the extracted FLTK directory, and run the following commands:

    ./configure
    make
    sudo make install

**Update the library path:** After installing FLTK, you may need to update your library path to include the FLTK libraries. This can be done by adding the following line to your ~/.bashrc file:

    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib

Setting VLC & it's library on linux 
=============================

    sudo apt-get install libvlc-dev
    sudo apt-get install libvlccore-dev
    sudo apt-get install vlc
    sudo apt-get update && sudo apt-get upgrade


Compiling Cpp files
===================

**Server:** 

    g++ -o server server.cpp -lvlc

**Client:** Make sure to place server's hostname in the clients cpp files.

    g++ client1.cpp -o client1 -lfltk


For Server hostname visible on network
=====================================

**Important:** If server's hostname is not visible on the network then run this command on server system.

    sudo apt-get install samba

Running output files
====================

    ./server
    ./client1
