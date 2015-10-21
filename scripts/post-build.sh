python tests/run_tests.py
coverage erase
coverage run tests/run_tests.py
coverage report --include=*saws/*
python -m coverage xml --include=*saws/*
pylint -f parseable -d I0011,R0801 saws | tee pylint.out