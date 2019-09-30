#!/usr/bin/env python

import socket
import sys
import serial
import configparser
import logging
import pyled
import client

# Read configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Configuration
LISTEN_ADDR = config.get('api', 'address')
LISTEN_PORT = config.getint('api', 'port')
MATRIX_TYPE = config.get('display', 'type')
MATRIX_WIDTH = config.getint('display', 'width')
MATRIX_HEIGHT = config.getint('display', 'height')
SERIAL_PORT = config.get('display', 'serial')
BAUD_RATE = config.getint('display', 'baud')

# setup default generator
try:
    GENERATOR = config.get('general', 'generator')
except configparser.NoOptionError:
    GENERATOR = 'Black'

# setup default brightness
try:
    BRIGHTNESS = config.getint('general', 'brightness')
except configparser.NoOptionError:
    BRIGHTNESS = 255

# setup default FPS
try:
    MAXFPS = config.getint('display', 'maxfps')
except configparser.NoOptionError:
    MAXFPS = 24

# Setup logging
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

# Open serial port
tty = serial.Serial(SERIAL_PORT, BAUD_RATE)

# Create Display with Driver
driver = pyled.driver.Serial(MATRIX_WIDTH, MATRIX_HEIGHT, MATRIX_TYPE, tty)
# driver = pyled.driver.Dummy(MATRIX_WIDTH, MATRIX_HEIGHT)

# Start Display Thread
display = pyled.PyLED(driver)
display.set_generator(GENERATOR)
display.set_brightness(BRIGHTNESS)
display.set_max_fps(MAXFPS)
display.start()

# Bind socket to local host and port
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
logging.info('Socket created')

try:
    sck.bind((LISTEN_ADDR, LISTEN_PORT))
except socket.error as msg:
    logging.error('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

logging.info('Socket bind complete')

# Start listening on socket
sck.listen(10)
logging.info('Socket now listening')

connections = []

while display.is_alive():
    try:
        # wait to accept a connection - blocking call
        (conn, (ip, port)) = sck.accept()

        newconn = client.ClientThread(conn, ip, port, display)
        newconn.start()
    except KeyboardInterrupt:
        display.stop()
        sck.close()
        tty.close()
        sys.exit()
