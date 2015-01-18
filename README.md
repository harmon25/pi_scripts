# pi_scripts
pi_scripts


## Requirements
### General for Raspberry
'''shell
apt-get install python git python-dev python-pip python-rpi.gpio 
'''

### General for Banana
'''shell
apt-get install python git python-dev
git clone git@github.com:LeMaker/RPi.GPIO_BP.git
cd RPi.GPIO_BP
python setup.py install
sudo python setup.py install
'''

### Requirements for GPS Scripts
- A GPS module, and gpsc working properly
'''shell
apt-get install gpsd gpsd-clients
'''
