Project Directories
===================

**Server:**  Contain server file.
**Client:**  Contain 2 client files. client1 for 1st client and client2 for 2nd client.
**Library:**  Contain srt parser header file. Must be include in server file.
**Subtile:**  Contain subtitle file that need to be parse and display on LCD.
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



Compiling Cpp files
===================

**Server:** 

    g++ server.cpp -o server

**Client:** Make sure to place server's hostname in the clients cpp files.

    g++ client1.cpp -o client1 -lfltk
    g++ client2.cpp -o client2 -lfltk


For Server hostname visible on network
=====================================

**Important:** If server's hostname is not visible on the network then run this command on server system.

    sudo apt-get install samba

Running output files
====================

    ./server
    ./client1
    ./client2
