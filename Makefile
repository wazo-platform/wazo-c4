
venv:
	virtualenv -p python3 venv --no-site-packages

setup:
	pip install -r requirements.txt

run-test:
	docker exec wazo-c4_wazo-tester_1 pytest /tests/

flake8:
	flake8 --ignore=E501,E402,W503 tests

black:
	black tests

pikeoff:
	docker exec -it wazo-c4_sbc_1 kamcmd pv.shvSet pike_off int 1

run:
	docker-compose up -d

run-dev:
	docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml up -d

stop:
	docker-compose down
	rm -r data

start-auth:
	docker-compose -f docker-compose.yaml -f docker-compose.wazo-auth.yaml -f docker-compose.dev.yaml up -d

auth-setup:
	docker exec wazo-c4_wazo-tester_1 wazotester /tests/wazo-auth/init_auth.yaml -a https://wazo-auth:9497

stop-auth:
	docker-compose -f docker-compose.yaml -f docker-compose.wazo-auth.yaml -f docker-compose.dev.yaml down

.PHONY:
	setup
	run-test
	flake8
	black
	pikeoff
	run
	run-dev
	stop
	start-auth
	auth-setup
	stop-auth
