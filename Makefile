install:
	sudo cp -f $(DIR)punicon.png /usr/share/pixmaps/
	sudo cp -f $(DIR)battery.py /usr/local/bin/
	sudo cp -f $(DIR)batterypun.service /etc/systemd/system/batterypun.service

uninstall:
	sudo rm -f /usr/local/bin/battery.py
	sudo rm -f /usr/share/pixmaps/punicon.png
	sudo rm -f /etc/systemd/system/batterypun.service

.PHONY: install unistall
