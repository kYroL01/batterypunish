batterypunish
=============

**batterypunish** is a python service to notify a message alert when the charge of battery is 20 %.
Use the `gtk` library to create and notify a small graphical notification on the screen.


## Makefile

`make install`

`make uninstall`

Now your file is under `/usr/local/bin`

Modify the permission and run in background

`chmod +x /usr/local/bin/battery.py`

`sudo /usr/local/bin/battery.py &`


## Dependencies

[gtk][pygtk]


[pygtk]: https://wiki.python.org/moin/PyGtk
