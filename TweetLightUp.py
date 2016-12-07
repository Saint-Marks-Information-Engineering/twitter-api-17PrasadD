import time
import RPi.GPIO as GPIO
from twython import TwythonStreamer
from time import sleep

# Search terms
TERMS = '#MAGA'

# GPIO pin number of LED
LED = 22

# Twitter application authentication
APP_KEY = 'uxeo6hLJSEPiuZtKH1deLeDes'
APP_SECRET = '6JlX3GaPDZ7BDLHtBax3xw1UHP6eynOGzv7VVxuLMMtlAerq8c'
OAUTH_TOKEN = '1301036743-DQboFr5XbcDq43EaWH0uThmI3UZrxyRpoPGE9f4'
OAUTH_TOKEN_SECRET = 'ZdK2znn7LqeV1jUl9KBfclcdc4ANr8b0PLEUT0ZC3LQ0y'
# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        print(data['text'].encode('utf-8'))
                        #print
                        #GPIO.output(LED, GPIO.HIGH)
                        time.sleep(2)
                        #GPIO.output(LED, GPIO.LOW)

# Setup GPIO as output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

# Create streamer
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN,
OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)

except KeyboardInterrupt:
        GPIO.cleanup()
