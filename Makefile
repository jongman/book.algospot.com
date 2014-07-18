all: page

page:
	python compile.py

deploy: page
	rsync -avh --progress -e ssh output/* algospot@algospot.com:/algospot/www_static/book
	
