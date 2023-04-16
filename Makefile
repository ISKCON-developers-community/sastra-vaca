create:
	docker build -t sastra-vaca .
	mkdir files

run:
	docker run -it -v /home/sasha/Coding/1_python/sastra-vaca/files:/usr/src/app/files --name sastra-vaca-con --rm sastra-vaca

stop:
	docker stop sastra-vaca-con
