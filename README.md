# dht11-mqtt-bridge
An executable python function for publishing DHT11 temperature and humidity data from a Raspberry Pi using Paho MQTT

Download the latest ca certificate to appropriate folder
cd /etc/ssl/certs
sudo rm learning-iot-ca.crt
sudo curl -0 https://learning-iot.aidanparkinson.xyz -o learning-iot-ca.crt

## Install device dependencies
```
sudo apt update
sudo apt-get install virtualenv python3-pip
pip3 --version
```

## Clone this repository
Navigate to add-on application folder
```
cd /opt
```
Clone repository
```
sudo git clone https://github.com/aidan-parkinson/dht11-mqtt-bridge.git
```

## Create virtual environment and install project dependencies
Navigate to project folder
```
cd /opt/dht11-mqtt-bridge/
```
Create a virtual environment
```
sudo virtualenv venv
```
Activate it
```
source venv/bin/activate
```
Install project dependencies
```
pip3 install -r requirements.txt
```
Deactivate the virtual environment
```
deactivate
```

## To run the bridge (start at this point if you have completed this process before on your device)
Navigate to project folder
```
cd /opt/dht11-mqtt-bridge/
```
Activate the virtual evironment with pre-installed dependencies
```
source venv/bin/activate
```
Run the `dht11-mqtt.py` controller
```
sudo python3 dht11-mqtt.py
```
