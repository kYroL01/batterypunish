DIR = ./src/

install:
	mkdir -p $(DIR)
	sudo cp -f punisher_icon.png $(DIR)
	sudo cp -f battery $(DIR)
	sudo rm -f punisher_icon.png
	sudo rm -f battery
	cd $(DIR)
	sudo cp -f $(DIR)punisher_icon.png /usr/share/pixmaps/
	sudo cp -f $(DIR)battery /usr/bin/

unistall:
	sudo rm -f /usr/bin/battery
	sudo rm -f /usr/share/pixmaps/punisher_icon.png

clear:
	rm -fr $(DIR)


PHONY: istall unistall clear
