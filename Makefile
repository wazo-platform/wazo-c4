.PHONY:
venv:
	virtualenv -p python3 venv --no-site-packages

.PHONY: setup
setup:
	pip install -r requirements.txt

.PHONY: test
test:
	docker exec wazo-c4_wazo-tester_1 pytest /tests/

.PHONY: flake8
flake8:
	flake8 --ignore=E501,E402,W503 tests

.PHONY: black
black:
	black tests

.PHONY: pikeoff
pikeoff:
	docker exec -it wazo-c4_sbc_1 kamcmd pv.shvSet pike_off int 1

.PHONY: run
run:
	docker-compose up -d

.PHONY: run-dev
run-dev:
	docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml up -d

.PHONY: stop
stop:
	docker-compose down
	rm -r data

.PHONY: start-auth
start-auth:
	docker-compose -f docker-compose.wazo-auth.yaml -f docker-compose.dev.yaml up -d

.PHONY: stop-auth
stop-auth:
	docker-compose -f docker-compose.wazo-auth.yaml -f docker-compose.dev.yaml down
