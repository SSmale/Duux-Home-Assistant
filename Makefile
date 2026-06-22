.PHONY: start test test-cov mutmut mutmut-results mutmut-show

start:
	scripts/develop

test:
	python -m pytest tests/ -q

test-cov:
	python -m pytest tests/ --cov=custom_components/duux --cov-report=term-missing -q

mutmut:
	mutmut run

mutmut-file:
	@test -n "$(FILE)" || (echo "Usage: make mutmut-file FILE=custom_components/duux/const.py" && exit 1)
	mutmut run $(FILE)

mutmut-results:
	mutmut results

mutmut-show:
	mutmut browse
