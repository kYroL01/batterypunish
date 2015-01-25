install:
	sudo cp -f $(DIR)punisher_icon.png /usr/share/pixmaps/
	sudo cp -f $(DIR)battery /usr/bin/

uninstall:
	sudo rm -f /usr/bin/battery
	sudo rm -f /usr/share/pixmaps/punisher_icon.png

clean:
	rm -fr $(DIR)


.PHONY: istall unistall clear
