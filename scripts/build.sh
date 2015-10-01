sudo apt-get python python-pip -y
sudo pip install -e .
sudo pip install -r requirements-dev.txt
python ./tests/test_dependencies.py
