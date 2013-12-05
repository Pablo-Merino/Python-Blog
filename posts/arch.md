Today I removed CrunchBang from my laptop (a Debian based distribution with Openbox as WM) to install Arch Linux. Arch lets you customize every single bit of your OS, from the kernel modules to the icon sets.

As I had some experience with dynamic WM, I went with `DWM`, `uxrvt` and some good color schemes. 

In Arch you need to get all the video, audio and network drivers and config all by yourself, and that depends on your machine, so it's not for all the users. My network devices were automatically detected, but I needed to install the `xf86-video-intel` driver for the Intel 4 Series card. You'd also need `alsa-utils`, which contains `alsa-mixer`, in order to un-mute the audio outputs. 

The Arch [Beginner's Guide](https://wiki.archlinux.org/index.php/Beginners'_Guide) is actually really good to get Arch installed, although you need some experience in UNIX based OSes.

In DWM you'd also need some way to have a quick glance of your computer status, which you can achieve with `conky` and setting it up to output to the console, then piping it up to `xset` and it'll show on the DWM's top bar (using for example `conky | while read; do xsetroot -name "$REPLY"; done &`). This is my `.xinitrc`:

```bash
setxkbmap es # Set the keymap to Spanish

wmname LG3D # Trick to get Netbeans working

xset +fp /usr/share/fonts/local # Detect fonts for URxvt

dropboxd & # Dropbox

conky | while read; do xsetroot -name "$REPLY"; done & # Conky piping to the DWM status bar

export _JAVA_OPTIONS='-Dawt.useSystemAAFontSettings=on -Dswing.aatext=true 
-Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel' # Make Netbeans fonts antialiased

xfce4-power-manager & # XFCE4 Power Manager

feh --bg-fill Wallpapers/andromeda.jpg # Background image 
exec dwm # And finally launch DWM
```

Something worth noting is the package manager, or `pacman` and the [AUR](https://aur.archlinux.org/) (Arch User Repository). AUR contains a ton of user-provided packages for a lot of applications (such as Dropbox or URxvt) and between them, there's the little `yaourt`, which lets you install packages from both `pacman` and the AUR with a simple command (`yaourt -S google-earth` which would install the AUR package `google-earth`).

Arch offers a lot of power, but also has the risk of breaking everything with a simple command (because of the level of customization). 

Arch also makes you learn some aspects of Linux that you probably wouldn't have learnt with Ubuntu for example, such as compiling your own packages, manually partitioning a hard disk,...

Definitely Arch Linux is a distro for Linux/UNIX fans and geeks who like to tinker with their OS and make it get used to their likings, instead of getting themselves used to the OS.