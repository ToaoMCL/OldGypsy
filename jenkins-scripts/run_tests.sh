sudo apt-get update
sudo apt-get install -y python3-venv python3-pip

cd s1-front-end
python3 -m venv venv
source venv/bin/activate
# Run service 1 front end tests
pip3 install -r requirements.txt
pip3 install -r test_requirements.txt
python3 -m pytest --cov-config=.coveragerc --cov=. --cov-report term-missing --junitxml junit.xml
deactivate
cd ..

# Run service 2 tests
cd s2-combination
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install -r test_requirements.txt
python3 -m pytest --cov-config=.coveragerc --cov=. --cov-report term-missing --junitxml junit.xml
deactivate
cd ..

# Run service 3 tests
cd s3-constalations
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install -r test_requirements.txt
python3 -m pytest --cov-config=.coveragerc --cov=. --cov-report term-missing --junitxml junit.xml

deactivate
cd ..

# Run service 4 tests
cd s4-tarot-cards
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install -r test_requirements.txt
python3 -m pytest --cov-config=.coveragerc --cov=. --cov-report term-missing --junitxml junit.xml
deactivate
cd ..
