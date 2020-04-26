.PHONY: buildup down res_log app_log auth_log

buildup:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d --build

down:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml down

res_log:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml logs -f --tail=100 resource

app_log:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml logs -f --tail=100 application

auth_log:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml logs -f --tail=100 authorization

