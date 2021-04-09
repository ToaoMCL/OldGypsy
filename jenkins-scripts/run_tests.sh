sudo apt-get update
sudo apt-get install -y python3-venv python3-pip

#cd s1-front-end
python3 -m venv venv
source venv/bin/activate
# Run service 1 front end tests
pip3 install -r s1-front-end/requirements.txt
pip3 install pytest pytest-cov flask_testing requests_mock
python3 -m pytest --cov-config=.coveragerc --cov=s1-front-end --cov-report term-missing --junitxml junit.xml

# Run service 2 tests
pip3 install -r s2-combination/requirements.txt
python3 -m pytest --cov-config=.coveragerc --cov=s2-combination --cov-report term-missing --junitxml junit.xml

# Run service 3 tests
pip3 install -r s3-constalations/requirements.txt
python3 -m pytest --cov-config=.coveragerc --cov=s3-constalations --cov-report term-missing --junitxml junit.xml

# Run service 4 tests
pip3 install -r s4-tarot-cards/requirements.txt
python3 -m pytest --cov-config=.coveragerc --cov=s4-tarot-cards --cov-report term-missing --junitxml junit.xml

deactivate
cd ..