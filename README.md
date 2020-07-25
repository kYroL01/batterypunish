batterypunish
=============

**batterypunish** is a python service to notify a message alert when the charge of battery is 20 %.
Use the `gtk` library to create and notify a small graphical notification on the screen.


## Makefile

`make install`

`make uninstall`

Now your file is under `/usr/local/bin`


## Reload systemd manager configuration
systemctl daemon-reload

## Launch the service
systemctl start batterypun

## Enable the service from startup
systemctl enable batterypun


## Dependencies

[gtk][pygtk]


[pygtk]: https://wiki.python.org/moin/PyGtk
