install:
	sudo cp -f $(DIR)punisher_icon.png /usr/share/pixmaps/
	sudo cp -f $(DIR)battery.py /usr/local/bin/

uninstall:
	sudo rm -f /usr/local/bin/battery.py
	sudo rm -f /usr/share/pixmaps/punisher_icon.png

.PHONY: install unistall