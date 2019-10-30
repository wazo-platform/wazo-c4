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
