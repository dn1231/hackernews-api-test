.PHONY: venv install test report clean

venv:
	python3 -m venv .venv

install:
	. .venv/bin/activate && pip install -r requirements.txt

test report:
	./run_tests.sh

clean:
	rm -rf reports
