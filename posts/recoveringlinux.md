So today I had to recover the `/bin` directory on a Ubuntu 64-bit server. Apparently it was accidentally removed, so neither `ls`, `cp` or other UNIX commands were working (they were removed, duh). 

After a bit of Googling, I came across a way to launch executables using `ld-linux.so.2`, which is an ELF interpreter and it did the trick of launching a couple broken-permission executables I copied from another server.

I just ran `/lib/ld-linux.so.2 /root/bin/mkdir /bin` in order to create the previously removed folder, then `/lib/ld-linux.so.2 /root/bin/cp /root/bin/* /bin` to copy the executables and `/lib/ld-linux.so.2 /root/bin/chmod +x /bin/*` to make them executable. It's working now!