build:
	docker-compose up --build -d

log:
	docker-compose logs

stop:
	docker-compose down

clean:
	docker-compose down --rmi all

clean_old:
	docker image prune -a && docker container prune