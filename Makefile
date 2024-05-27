runall:
	docker-compose up --build -d

stop:
	docker-compose down

restart: stop runall

logs:
	docker-compose logs -f

cleanall:
	docker image prune && \
	docker container prune
