install:
	sudo cp -f $(DIR)punicon.png /usr/share/pixmaps/
	sudo cp -f $(DIR)battery.py /usr/local/bin/

uninstall:
	sudo rm -f /usr/local/bin/battery.py
	sudo rm -f /usr/share/pixmaps/punicon.png

.PHONY: install unistall
