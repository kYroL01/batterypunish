batterypunish
=============

**batterypunish** is a python module that notify on the screen a message alert when the charge of battery is at 10 %.
Use the 'pynotify' library to create and notify a small graphical notification on the screen.

Install
=======

Once in the batterypunish folder, launch the **makefile** with

`make install`

or, alternatively:

1. copy `punisher_icon.png` into `/usr/share/pixmaps/`
2. copy `battery` into `/usr/bin/`

Unistall
========

In *makefile* directory,

1. `make uninstall`
2. `make clear`

Example
=======
This is an example of how to use it for [Openbox][opbx] window manager

Once installed, put the command in file `autostart`:
```
# Run the system-wide support stuff
#.$GLOBALAUTOSTART

## Programs to execute from the start-up

# batterypunish cmd
battery &
```
The file must be inside the config directory of openbox in the home folder, for example:
`:~/.config/.openbox`

This file is called the *openbox-autostart* file located in `/usr/lib/openbox`

Dependencies
============

batterypunish needs [PyGTK][pygtk] and [pynotify][pynot]


[pygtk]: http://www.pygtk.org/downloads.html
[pynot]: https://github.com/seb-m/pyinotify
[opbx]: http://openbox.org/wiki/Main_Page
