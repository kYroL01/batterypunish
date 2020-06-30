batterypunish
=============

**batterypunish** is a python module that notify on the screen a message alert when the charge of battery is at 10 %.
Use the 'pynotify' library to create and notify a small graphical notification on the screen.

## Requirements

batterypunish needs [PyGTK][pygtk] and [python-notify][pynot]

### Debian

`sudo apt-get install libnotify-cil-dev`

`sudo apt-get install python-notify`

## Install

`make install`

or, alternatively:

1. `cp punisher_icon.png /usr/share/pixmaps/`
2. `cp battery.py /usr/local/bin/`
3. `chmod +x /usr/local/bin/battery.py`

## Unistall

In *makefile* directory,

1. `make uninstall`
2. `make clear`


[pygtk]: http://www.pygtk.org/downloads.html
[pynot]: https://debian.pkgs.org/9/debian-main-amd64/python-notify_0.1.1-4_amd64.deb.html
[opbx]: http://openbox.org/wiki/Main_Page
