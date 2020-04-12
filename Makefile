.PHONY: buildup down

buildup:
	docker-compose up -d --build

down:
	docker-compose down

res_log:
	docker-compose logs -f --tail=10 resource

app_log:
	docker-compose logs -f --tail=10 application

auth_log:
	docker-compose logs -f --tail=10 authorization

