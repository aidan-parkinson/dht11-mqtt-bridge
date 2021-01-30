import paho.mqtt.client as mqtt
import ssl
import getmac
import adafruit_dht
import time
import board
import json
from datetime import datetime

gma = getmac.get_mac_address()

pin = board.D4

dht_device = adafruit_dht.DHT11(pin)

client = mqtt.Client()

broker = 'mqtts.aidanparkinson.xyz'
port = 8883
client.tls_set('/etc/ssl/certs/learning-iot-ca.crt', cert_reqs=ssl.CERT_NONE)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client.connect(broker, port)
client.loop_start();

client.on_connect = on_connect
client.on_message = on_message

while True:

    try:
        humidity = dht_device.humidity
        temperature = dht_device.temperature

        reading = json.dumps({'mac_address': gma, 'humidity': humidity, 'temperature': temperature, 'datetime': datetime.now()}, sort_keys=True, indent=4, default=str)

        print(reading)

        client.publish("dht11", reading)

    except RuntimeError:
        print('Failed')

    time.sleep(5);
