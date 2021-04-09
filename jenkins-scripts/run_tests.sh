sudo apt-get update
sudo apt-get install -y python3-venv python3-pip

cd s1-front-end
python3 -m venv venv
source venv/bin/activate
pip3 isntall -r requirements.txt
pip3 install pytest pytest-cov flask_testing requests_mock
python3 -m pytest --cov=. --cov-report term-missing --junitxml junit.xml
deactivate
cd ..