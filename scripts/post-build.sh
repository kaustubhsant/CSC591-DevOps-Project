mkdir htmlcov
sudo python tests/run_tests.py
coverage erase
sudo coverage run --branch tests/run_tests.py
coverage report --include=*saws/*
coverage html -d htmlcov
python -m coverage xml --include=*saws/*
pylint -f parseable -d I0011,R0801 saws | tee pylint.out 
