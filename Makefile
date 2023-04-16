create:
	docker build -t sastra-vaca .
	mkdir files

run:
	docker run -it -v $(shell pwd)/files:/usr/src/app/files --name sastra-vaca-con --rm sastra-vaca

stop:
	docker stop sastra-vaca-con


delete:
	docker rmi sastra-vaca
