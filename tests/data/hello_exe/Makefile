all: hello.exe

hello.res: hello.rc
	windres -o hello.res -O coff -F pe-i386 hello.rc 

hello.exe: hello.res hello.c
	gcc -o hello.exe -mwindows -m32 hello.c hello.res